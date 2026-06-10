from datetime import date
import logging

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QLineEdit
from docgen.design import Ui_MainWindow
from docgen.entities import Project, Font, font_styles
from docgen.main import get_project_data, get_projects, generate_acts, generate_statements, generate_tasks
from docgen.settings_manager import SettingsManager

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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

        self.tableWIthDataAction.triggered.connect(self.select_folder_with_workers_data)

        self.current_project = None

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

        if self.current_project.head:
            self.current_project.head.is_head = False


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



        
        


def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()