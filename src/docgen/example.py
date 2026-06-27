from datetime import date
from functools import partial
from typing import Dict
import logging

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit, QDialog
from docgen.design.design import Ui_MainWindow
from docgen.design.ui_settings import Ui_Dialog
from docgen.entities import Font, font_styles, WorkType
from docgen.main import get_project_data, get_projects, generate_acts, generate_statements, generate_tasks
from docgen.settings_manager import SettingsManager

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Настройки")

        self.settings = parent.settings

        self.ui.apiTokenLineEdit.setText(self.settings.get("api_token"))
        self.ui.workerTableLineEdit.setText(self.settings.get("worker_table_path"))
        self.ui.taskPathLineEdit.setText(self.settings.get("task_template_path"))
        self.ui.statementPathLineEdit.setText(self.settings.get("statement_template_path"))
        self.ui.actPathLineEdit.setText(self.settings.get("act_template_path"))
        self.ui.savePathLineEdit.setText(self.settings.get("output_dir"))

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


        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
    
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
        settings["api_token"] = self.ui.apiTokenLineEdit.text()
        settings["worker_table_path"] = self.ui.workerTableLineEdit.text()
        settings["task_template_path"] = self.ui.taskPathLineEdit.text()
        settings["statement_template_path"] = self.ui.statementPathLineEdit.text()
        settings["act_template_path"] = self.ui.actPathLineEdit.text()
        settings["output_dir"] = self.ui.savePathLineEdit.text()
        return settings


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.settings = SettingsManager()

        self.check_required_settings()
        
        projects = get_projects(self.settings)

        self.projectsComboBox.addItems(projects.keys())
        self.styleComboBox.addItems(font_styles)
        self.browseButton.clicked.connect(self.select_folder)
        self.projectInfoButton.clicked.connect(self.get_project_info)
        self.generateButton.clicked.connect(self.generate)

        self.tableWIthDataAction.triggered.connect(self.open_settings)

        self.current_project = None

    def open_settings(self):
        dialog = SettingsDialog(self)          
        result = dialog.exec()                 

        if result == QDialog.Accepted:
            value = dialog.get_settings()
            self._set_settings(value)
            print(f"Получены настройки: {value}")
        else:
            print("Настройки отменены")

    def check_required_settings(self):
        if not self.settings.has("api_token"):
            token, ok = QInputDialog.getText(
                self,
                "API Токен",
                "Введите API токен для доступа к данным:",
                QLineEdit.EchoMode.Password
            )
            if ok and token:
                self.settings.set("api_token", token)
            else:
                QMessageBox.critical(self, "Ошибка", "API токен обязателен для работы приложения.")
        
        required = [
            ("worker_table_path", "Выберите файл с данными о работниках", "*.xlsx"),
            ("act_template_path", "Выберите файл с шаблоном акта (.docx)", "*.docx"),
            ("task_template_path", "Выберите файл с шаблоном задания (.docx)", "*.docx"),
            ("statement_template_path", "Выберите файл с шаблоном заверения (.docx)", "*.docx"),
            ("output_dir", "Выберите папку для сохранения файлов", None),
        ]
        for key, title, file_filter in required:
            if not self.settings.has(key):
                if file_filter:
                    path, _ = QFileDialog.getOpenFileName(self, title, "", file_filter)
                else:
                    path = QFileDialog.getExistingDirectory(self, title)
                if path:
                    self.settings.set(key, path)
                else:
                    QMessageBox.critical(self, "Ошибка", f"Не выбран {title}")

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

        self.current_project = get_project_data(project_name, self.settings)

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

    def _set_settings(self, settings: Dict):
        for key, value in settings.items():
            if self.settings.has(key) and self.settings.get(key) != value:
                logging.debug(f"Изменение настройки {key} с {self.settings.get(key)} на {value}")
                self.settings.set(key, value)

def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()