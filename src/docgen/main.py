from datetime import date
from functools import partial
import logging
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog
from docgen.design.design import Ui_MainWindow
from docgen.design.ui_settings import Ui_Dialog
from docgen.entities import Font, font_styles, WorkType
from docgen.core import get_project_data, get_projects, generate_acts, generate_statements, generate_tasks
from docgen.settings_manager import SettingsManager, SettingsKey

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class SettingsDialog(QDialog):
    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Настройки")

        self.settings = settings_manager

        self.ui.apiTokenLineEdit.setText(self.settings.get(SettingsKey.API_TOKEN, ""))
        self.ui.workerTableLineEdit.setText(self.settings.get(SettingsKey.WORKER_TABLE_PATH, ""))
        self.ui.taskPathLineEdit.setText(self.settings.get(SettingsKey.TASK_TEMPLATE_PATH, ""))
        self.ui.statementPathLineEdit.setText(self.settings.get(SettingsKey.STATEMENT_TEMPLATE_PATH, ""))
        self.ui.actPathLineEdit.setText(self.settings.get(SettingsKey.ACT_TEMPLATE_PATH, ""))
        self.ui.savePathLineEdit.setText(self.settings.get(SettingsKey.OUTPUT_DIR, ""))

        self.ui.workerBrowseButton.clicked.connect(
            partial(self.select_folder,
                    self.ui.workerTableLineEdit,
                    "Таблица с данными о работниках", 
                    "*.xlsx"
            )
        )
        self.ui.taskBrowseButton.clicked.connect(
            partial(self.select_folder,
                    self.ui.taskPathLineEdit,
                    "Шаблон задания", 
                    "*.docx"
            )
        )
        self.ui.statementBrowseButton.clicked.connect(
            partial(self.select_folder,
                    self.ui.statementPathLineEdit,
                    "Шаблон заверения", 
                    "*.docx"
            )
        )
        self.ui.actBrowseButton.clicked.connect(
            partial(self.select_folder,
                    self.ui.actPathLineEdit,
                    "Шаблон акта", 
                    "*.docx"
            )
        )
        self.ui.saveBrowseButton.clicked.connect(
            partial(self.select_folder,
                    self.ui.savePathLineEdit,
                    "Папка для сохранения", 
                    None
            )
        )

        self.ui.buttonBox.accepted.connect(self.save_and_accept)
        self.ui.buttonBox.rejected.connect(self.reject)
    
    def save_and_accept(self):
        new_settings = {
            SettingsKey.API_TOKEN: self.ui.apiTokenLineEdit.text(),
            SettingsKey.WORKER_TABLE_PATH: self.ui.workerTableLineEdit.text(),
            SettingsKey.TASK_TEMPLATE_PATH: self.ui.taskPathLineEdit.text(),
            SettingsKey.STATEMENT_TEMPLATE_PATH: self.ui.statementPathLineEdit.text(),
            SettingsKey.ACT_TEMPLATE_PATH: self.ui.actPathLineEdit.text(),
            SettingsKey.OUTPUT_DIR: self.ui.savePathLineEdit.text()
        }
        self.settings.update(new_settings)
        self.accept()
    
    def select_folder(self, line_edit,  name: str, file_type: str):
        initial_dir = line_edit.text() or ""
        if file_type:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                f"Выберите файл {name}",
                initial_dir,
                file_type
            )
        else:
            file_path = QFileDialog.getExistingDirectory(
                self,
                f"Выберите папку {name}",
                initial_dir
            )
        if file_path:
            line_edit.setText(file_path)

    def get_settings(self):
        settings = {}
        settings[SettingsKey.API_TOKEN] = self.ui.apiTokenLineEdit.text()
        settings[SettingsKey.WORKER_TABLE_PATH] = self.ui.workerTableLineEdit.text()
        settings[SettingsKey.TASK_TEMPLATE_PATH] = self.ui.taskPathLineEdit.text()
        settings[SettingsKey.STATEMENT_TEMPLATE_PATH] = self.ui.statementPathLineEdit.text()
        settings[SettingsKey.ACT_TEMPLATE_PATH] = self.ui.actPathLineEdit.text()
        settings[SettingsKey.OUTPUT_DIR] = self.ui.savePathLineEdit.text()
        return settings


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.settings = SettingsManager()

        self._check_required_settings()
        
        self._setup_projects()
        
        self.styleComboBox.addItems(font_styles)
        self.browseButton.clicked.connect(self.select_folder)
        self.projectInfoButton.clicked.connect(self.get_project_info)
        self.generateButton.clicked.connect(self.generate)

        self.tableWIthDataAction.triggered.connect(self.open_settings)
        self.projectsReloadAction.triggered.connect(self._setup_projects)

        self.current_project = None

    def open_settings(self):
        dialog = SettingsDialog(self.settings, self)          
        result = dialog.exec()                 

        if result == QDialog.Accepted:
            value = dialog.get_settings()
            print(f"Получены настройки: {value}")
        else:
            print("Настройки отменены")

    def _check_required_settings(self):
        for s in SettingsKey.all_keys():
            if not self.settings.get(s):
                self.open_settings()
                break

    def select_folder(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл шрифта", "", "*.glyphs (*.glyphs*)")
        if file_path:
            self.pathLineEdit.setText(file_path)

    def get_project_info(self):
        project_name = self.projectsComboBox.currentText()
        if not project_name:
            QMessageBox.warning(self, "Ошибка", "Введите название проекта")
            return
        
        self.headWorkerBox.clear()
        if self.current_project:
            self.current_project.workers = []

        try:
            self.current_project = get_project_data(project_name, self.settings)
        except Exception as e:
            if isinstance(e, KeyError):
                QMessageBox.warning(self, "Ошибка", f"В таблице нет работника: {str(e)}\n\nДобавьте информацию о работнике и загрузите проект снова.")
            if isinstance(e, ValueError):
                QMessageBox.warning(self, "Ошибка", f"В таблице нет ФИО работника: {str(e)}\n\nДобавьте информацию о работнике и загрузите проект снова.")
            return
            

        self.startDate.setDate(self.current_project.start_date)
        self.endDate.setDate(self.current_project.end_date)
        self.currentDate.setDate(date.today())
        self.headWorkerBox.addItems([w.full_name() for w in self.current_project.workers])

    def select_folder_with_workers_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл с данными о работниках", "", "*.xlsx (*.xlsx)")
        if file_path:
            QMessageBox.information(self, "Успех", f"Файл {file_path} выбран")
        else:
            QMessageBox.warning(self, "Ошибка", "Файл не выбран")

    def generate(self):
        if not self.pathLineEdit.toPlainText():
            QMessageBox.warning(self, "Ошибка", "Выберите файл шрифта")
            return
        
        if not self.styleComboBox.currentText():
            QMessageBox.warning(self, "Ошибка", "Выберите название стиля")
            return

        if not self.current_project:
            QMessageBox.warning(self, "Ошибка", "Данные проекта не загружены")
            return
        
        start_date = self.startDate.date().toPython()
        end_date = self.endDate.date().toPython()
        current_date = self.currentDate.date().toPython()

        if self.current_project and self.current_project.start_date != start_date:
            logging.debug(f"Дата начала проекта изменена с {self.current_project.start_date} на {start_date}")
            self.current_project.start_date = start_date
            
        if self.current_project and self.current_project.end_date != end_date:
            logging.debug(f"Дата окончания проекта изменена с {self.current_project.end_date} на {end_date}")
            self.current_project.end_date = end_date

        if self.current_project and self.current_project.current_date != current_date:
            logging.debug(f"Текущая дата проекта изменена с {self.current_project.current_date} на {current_date}")
            self.current_project.current_date = current_date

        if self.current_project.head:
            self.current_project.head.is_head = False
        
        if self.workTypeCheckBox.isChecked():
            self.current_project.type = WorkType.Create
        else:
            self.current_project.type = WorkType.Update
        

        self.current_project.style = self.styleComboBox.currentText()
        self.current_project.font = Font(self.pathLineEdit.toPlainText())
        
        self.current_project.head = self.current_project.workers[self.headWorkerBox.currentIndex()]

        self.current_project.head.is_head = True

        self.current_project.workers.sort(key=lambda w: (not w.is_head, w.full_name()))
        self.headWorkerBox.clear()
        self.headWorkerBox.addItems([w.full_name() for w in self.current_project.workers])
        logging.debug("Вывод работников:")
        for worker in self.current_project.workers:
            logging.debug(worker.full_name(True))


        self.progressBar.setValue(0)
        self.progressBar.setVisible(True)

        self.generateButton.setEnabled(False)
        self.projectInfoButton.setEnabled(False)
        self.browseButton.setEnabled(False)

        if self.taskCheckBox.isChecked():
            generate_tasks(self.current_project, self.settings)
        
        self.progressBar.setValue(33)

        if self.statementCheckBox.isChecked():    
            generate_statements(self.current_project, self.settings)

        self.progressBar.setValue(66)
        
        if self.actsCheckBox.isChecked():
            generate_acts(self.current_project, self.settings)

        self.progressBar.setValue(100)
        
        self.generateButton.setEnabled(True)
        self.projectInfoButton.setEnabled(True)
        self.browseButton.setEnabled(True)

        QMessageBox.information(self, "Успех", "Генерация завершена")

    def _get_projects(self, interval=2, timeout=10):
        start = time.time()
        last_error = None
        while time.time() - start < timeout:
            try:
                projects = get_projects(self.settings)
                if projects is not None:  
                    return projects
            except Exception as e:
                last_error = e
                logging.debug(f"Попытка не удалась: {e}")
            elapsed = time.time() - start
            remaining = timeout - elapsed
            if remaining <= 0:
                break
            time.sleep(min(interval, remaining))
        if last_error:
            QMessageBox.critical(
            self,
            "Ошибка получения проектов",
            f"Не удалось получить проекты за {timeout} секунд.\n"
            f"Последняя ошибка: {last_error}"
        )
        else:
            return None
        
    def _setup_projects(self):
        self.projectsComboBox.clear()
        projects = self._get_projects(2, 10)
        projects_names = projects.keys() if projects else []
        self.projectsComboBox.addItems(projects_names)

                

def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()