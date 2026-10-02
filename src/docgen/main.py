from datetime import date
import logging
import sys

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QFileDialog, 
    QMessageBox, 
    QDialog
)
from docgen.design.design import Ui_MainWindow
from docgen.design.ui_settings import Ui_Dialog
from docgen.entities import font_styles, WorkType
from docgen.core import get_project_data
from docgen.settings_manager import SettingsManager, SettingsKey
from docgen.orchestration import (
    build_project_from_ui_state,
    fetch_projects_with_retry,
    generate_documents
)
from docgen.exceptions import (
    DataSourceError,
    DocgenError,
    ProjectError,
    ProjectNotFoundError,
    WorkerDataError,
)

SETTINGS_FIELDS = [
    ("apiTokenLineEdit",    SettingsKey.API_TOKEN,             None,                     None),
    ("workerTableLineEdit", SettingsKey.WORKER_TABLE_PATH,     "Таблица с данными о работниках", "*.xlsx"),
    ("taskPathLineEdit",    SettingsKey.TASK_TEMPLATE_PATH,    "Шаблон задания",          "*.docx"),
    ("statementPathLineEdit", SettingsKey.STATEMENT_TEMPLATE_PATH, "Шаблон заверения",    "*.docx"),
    ("actPathLineEdit",     SettingsKey.ACT_TEMPLATE_PATH,     "Шаблон акта",             "*.docx"),
    ("savePathLineEdit",    SettingsKey.OUTPUT_DIR,            "Папка для сохранения",    None),
]

class SettingsDialog(QDialog):
    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Настройки")
        self.settings = settings_manager

        for line_edit_name, key, label, mask in SETTINGS_FIELDS:
            line_edit = getattr(self.ui, line_edit_name)
            line_edit.setText(self.settings.get(key, ""))

            browse_name = line_edit_name.replace("LineEdit", "BrowseButton")
            browse = getattr(self.ui, browse_name, None)
            if browse is not None and label is not None:
                browse.clicked.connect(
                    lambda _=False, le=line_edit, lbl=label, m=mask: self._select_path(le, lbl, m)
                )

        self.ui.buttonBox.accepted.connect(self._save_and_accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        
    def _select_path(self, line_edit, label: str, mask: str | None) -> None:
        initial = line_edit.text() or ""
        if mask:
            file_path, _ = QFileDialog.getOpenFileName(self, f"Выберите файл: {label}", initial, mask)
        else:
            file_path = QFileDialog.getExistingDirectory(self, f"Выберите папку: {label}", initial)
        if file_path:
            line_edit.setText(file_path)

    def collect_settings(self) -> dict:
        return {
            key: getattr(self.ui, name).text()
            for name, key, _, _ in SETTINGS_FIELDS
        }

    def _save_and_accept(self) -> None:
        self.settings.update(self.collect_settings())
        self.accept()


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = SettingsManager()
        self.current_project = None

        self.styleComboBox.addItems(font_styles)

        self.browseButton.clicked.connect(self._choose_font)
        self.projectInfoButton.clicked.connect(self._load_project)
        self.generateButton.clicked.connect(self._generate)

        self.tableWIthDataAction.triggered.connect(self._open_settings)
        self.projectsReloadAction.triggered.connect(self._reload_projects)

        if not self._settings_complete():
            self._open_settings()

        self._reload_projects()

    def _settings_complete(self) -> bool:
        return all(self.settings.get(key) for key in SettingsKey.all_keys())

    def _open_settings(self) -> None:
        dialog = SettingsDialog(self.settings, self)
        if dialog.exec() == QDialog.Accepted:
            logging.debug("Настройки сохранены: %s", dialog.collect_settings())
            
    def _reload_projects(self) -> None:
        self.projectsComboBox.clear()
        if not self._settings_complete():
            return

        try:
            projects = fetch_projects_with_retry(self.settings, interval=2, timeout=10)
        except DataSourceError as e:
            QMessageBox.critical(self, e.default_title, f"{e}\n\n{e.default_message}")
            return
        except Exception as e:
            logging.exception("Не удалось получить проекты")
            QMessageBox.critical(
                self, "Ошибка получения проектов",
                f"{type(e).__name__}: {e}",
            )
            return
        self.projectsComboBox.addItems(projects.keys())

    def _load_project(self) -> None:
        project_name = self.projectsComboBox.currentText()
        if not project_name:
            QMessageBox.warning(self, "Ошибка", "Введите название проекта")
            return

        try:
            new_project = get_project_data(project_name, self.settings)
        except ProjectNotFoundError as e:
            QMessageBox.warning(self, e.default_title, f"{e}\n\nОбновите список проектов.")
            return
        except WorkerDataError as e:
            QMessageBox.warning(self, e.default_title, f"{e}\n\n{e.default_message}")
            return
        except DataSourceError as e:
            QMessageBox.critical(self, e.default_title, f"{e}\n\n{e.default_message}")
            return
        except DocgenError as e:
            QMessageBox.warning(self, e.default_title, str(e))
            return
        except Exception as e:
            logging.exception("Непредвиденная ошибка загрузки проекта")
            QMessageBox.critical(self, f"Внутренняя ошибка ({type(e).__name__})", str(e))
            return

        self.current_project = new_project
        self.startDate.setDate(new_project.start_date)
        self.endDate.setDate(new_project.end_date)
        self.currentDate.setDate(date.today())

        self.headWorkerBox.clear()
        self.headWorkerBox.addItems(w.full_name() for w in new_project.workers)
        if self.headWorkerBox.count() > 0:
            self.headWorkerBox.setCurrentIndex(0)

    def _choose_font(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл шрифта", "", "*.glyphs (*.glyphs*)"
        )
        if file_path:
            self.pathLineEdit.setText(file_path)

    def _generate(self) -> None:
        if not self.current_project:
            QMessageBox.warning(self, "Ошибка", "Данные проекта не загружены")
            return

        work_type = WorkType.Create if self.workTypeCheckBox.isChecked() else WorkType.Update

        try:
            build_project_from_ui_state(
                self.current_project,
                start_date=self.startDate.date().toPython(),
                end_date=self.endDate.date().toPython(),
                current_date=self.currentDate.date().toPython(),
                style=self.styleComboBox.currentText(),
                font_path=self.pathLineEdit.toPlainText(),
                head_index=self.headWorkerBox.currentIndex(),
                work_type=work_type,
            )
        except ProjectError as e:
            QMessageBox.warning(self, e.default_title, str(e))
            return

        self.headWorkerBox.clear()
        self.headWorkerBox.addItems([w.full_name() for w in self.current_project.workers])
        if self.headWorkerBox.count() > 0:
            self.headWorkerBox.setCurrentIndex(0)

        self._set_busy(True)
        try:
            generate_documents(
                self.current_project,
                self.settings,
                do_task=self.taskCheckBox.isChecked(),
                do_statement=self.statementCheckBox.isChecked(),
                do_act=self.actsCheckBox.isChecked(),
                progress_cb=self.progressBar.setValue,
            )
        except DocgenError as e:
            QMessageBox.warning(self, e.default_title, f"{e}\n\n{e.default_message}")
            return
        except Exception as e:
            logging.exception("Ошибка генерации")
            QMessageBox.critical(self, f"Ошибка генерации ({type(e).__name__})", str(e))
            return
        finally:
            self._set_busy(False)

        QMessageBox.information(self, "Успех", "Генерация завершена")


    def _set_busy(self, busy: bool) -> None:
        for w in (self.generateButton, self.projectInfoButton, self.browseButton):
            w.setEnabled(not busy)
        self.progressBar.setVisible(busy)
        if not busy:
            self.progressBar.setValue(0)


                

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()