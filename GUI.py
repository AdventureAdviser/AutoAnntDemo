# GUI.py
import json
import os
import shutil
import sys

from PySide6.QtCore import QDir
from PySide6.QtGui import QPixmap, QPalette, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QTreeWidgetItem, QMessageBox, \
    QTreeWidget
from ui_autoannt import Ui_MainWindow, BackgroundLabel, CustomTreeWidget  # Импортируем сгенерированный класс интерфейса


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()

        # Создаем экземпляр кастомного виджета дерева
        self.customDirectoryBar = CustomTreeWidget(self)
        self.customDirectoryBar.setObjectName(u"DirectoryBar")
        self.customDirectoryBar.setHeaderLabels(["Directory Structure"])
        self.customDirectoryBar.setStyleSheet(u"#DirectoryBar {\n"
                                              "background-color: rgba(246, 247, 240, 73);\n"
                                              "}")
        # Подключаем UI компоненты
        self.setupUi(self)

        # Настраиваем фон
        self.backgroundLabel = BackgroundLabel(self)
        self.backgroundLabel.lower()
        self.backgroundLabel.resize(self.size())
        self.backgroundLabel.show()

        # По умолчанию показываем начальную страницу
        self.stackedWidget.setCurrentIndex(0)

        # Подключение сигналов к слотам
        self.new_pushButton.clicked.connect(self.onNewProjectClicked)
        self.prodgect_pushButton.clicked.connect(self.reset_ui_to_initial_state)
        self.choose_pushButton.clicked.connect(self.onChooseProjectClicked)

        # Заменяем DirectoryBar на CustomTreeWidget и добавляем его в layout
        self.gridLayout_5.addWidget(self.customDirectoryBar, 0, 2, 2, 1)  # Позиционирование как у DirectoryBar

        # Инициализация переменных
        self.project_registry_file = "project_registry.json"
        self.project_directory = None

        # Скрываем все виджеты, которые не должны быть видимы при старте
        self.hide_other_widgets()

    def resizeEvent(self, event):
        # Обновляем размер фона при изменении размера окна
        self.backgroundLabel.resize(self.size())
        super(MyApplication, self).resizeEvent(event)

    def onDirectoryBarClicked(self, point):
        selected_files, _ = QFileDialog.getOpenFileNames(
            self, "Select Resources", QDir.homePath(),
            "All Files (*);;Images (*.png *.jpg *.jpeg);;Videos (*.mp4 *.avi)"
        )
        if selected_files:
            self.add_resources_to_project(selected_files)

    def add_resources_to_project(self, files):
        video_dir = os.path.join(self.project_directory, 'source_video')
        photo_dir = os.path.join(self.project_directory, 'source_photo')

        # Создание директорий, если они не существуют
        os.makedirs(video_dir, exist_ok=True)
        os.makedirs(photo_dir, exist_ok=True)

        for file_path in files:
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Копирование фотографий
                shutil.copy(file_path, photo_dir)
            elif file_path.lower().endswith(('.mp4', '.avi')):
                # Копирование видео
                shutil.copy(file_path, video_dir)

        # Обновление дерева директорий после добавления файлов
        self.load_directory_structure(self.project_directory)
        QMessageBox.information(self, "Resources Added", "Resources have been successfully added to the project.")

    def onNewProjectClicked(self):
        project_folder = QFileDialog.getExistingDirectory(self, "Select Project Folder")
        if project_folder:
            self.load_directory_structure(project_folder)
            project_name, ok = QInputDialog.getText(self, "Project Name", "Enter the name of the new project:")
            if ok and project_name:
                project_path = os.path.join(project_folder, project_name)
                if not os.path.exists(project_path):
                    os.makedirs(project_path)
                    self.update_project_registry(project_path)
                    self.setup_project_ui(project_path)

    def update_project_registry(self, new_project_path):
        # Чтение существующих данных
        try:
            with open(self.project_registry_file, 'r') as file:
                try:
                    projects = json.load(file)
                except json.JSONDecodeError:
                    projects = []  # Если файл пуст или данные некорректны, используем пустой список
        except FileNotFoundError:
            projects = []

        # Добавление нового проекта
        if new_project_path not in projects:
            projects.append(new_project_path)
            with open(self.project_registry_file, 'w') as file:
                json.dump(projects, file, indent=4)  # Форматированный вывод для удобства
            print(f"Project {new_project_path} added to registry.")

        self.load_projects_to_ui(projects)  # Обновление UI с доступными проектами

    def onChooseProjectClicked(self):
        # При нажатии на кнопку выбора проекта
        if not hasattr(self, 'projects') or not self.projects:
            # Если список проектов пуст или не загружен, попробуем загрузить из файла
            if os.path.exists(self.project_registry_file):
                with open(self.project_registry_file, 'r') as file:
                    try:
                        self.projects = json.load(file)
                    except json.JSONDecodeError:
                        self.projects = []
            else:
                print("No project registry file found.")
                self.projects = []

        if self.projects:
            project, ok = QInputDialog.getItem(self, "Select a Project", "Choose a project:", self.projects, 0, False)
            if ok and project:
                self.setup_project_ui(project)
        else:
            print("No projects found. Please create a new project first.")

    def setup_project_ui(self, project_path):
        self.project_directory = project_path
        self.stackedWidget.hide()
        self.load_directory_structure(project_path)
        self.show_other_widgets()

    def show_other_widgets(self):
        # Показываем виджеты, связанные с проектом
        self.ClassesBar.show()
        self.AnntBar.show()
        self.NeuralBar.show()
        self.ModelBar.show()
        self.customDirectoryBar.show()
        # self.VideoSroll.show()
        self.ProdgectBar.show()

    def reset_ui_to_initial_state(self):
        # Метод для сброса UI к начальному состоянию
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.show()  # Показываем стек виджет
        self.hide_other_widgets()  # Скрываем остальные виджеты

    def hide_other_widgets(self):
        # Скрытие всех виджетов кроме стек виджета
        self.ClassesBar.hide()
        self.AnntBar.hide()
        self.NeuralBar.hide()
        self.ModelBar.hide()
        self.customDirectoryBar.hide()
        self.VideoSroll.hide()
        self.ProdgectBar.hide()

    def load_directory_structure(self, path):
        self.customDirectoryBar.clear()  # Очистка предыдущих элементов
        self.populate_tree_widget(self.customDirectoryBar, path)

    def populate_tree_widget(self, tree_widget, directory, parent_item=None):
        if parent_item is None:
            parent_item = tree_widget.invisibleRootItem()
        for item in sorted(os.listdir(directory)):
            child_item = QTreeWidgetItem(parent_item, [item])
            child_path = os.path.join(directory, item)
            if os.path.isdir(child_path):
                self.populate_tree_widget(tree_widget, child_path, child_item)
            else:
                child_item.setExpanded(False)  # Устанавливаем элементы не раскрытыми

    def load_projects_to_ui(self, projects):
        # Эта функция должна вызываться каждый раз, когда нужно обновить список проектов в UI
        # Например, после добавления нового проекта или при открытии окна выбора проекта
        if projects:
            self.projects = projects  # Сохраняем список проектов
        else:
            self.projects = []


    def display_photo(self, file_path):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.indexOf(self.photo_page))
        pixmap = QPixmap(file_path)
        self.photo_widget.setPixmap(
             pixmap.scaled(self.photo_widget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.stackedWidget.show()

    def open_project(self, project_path):
        # Здесь код для открытия проекта
        print(f"Opening project at {project_path}")
        # Обновление интерфейса или другие действия с проектом

    def create_new_project(self, folder, name):
        # Здесь ваш код для инициализации нового проекта
        pass