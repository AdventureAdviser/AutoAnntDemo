import json
import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QColorDialog
from ui import Ui_MainWindow, BackgroundLabel, CustomTreeWidget
from directory_manager import DirectoryManager


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.directory_manager = DirectoryManager(self)

        # Создаем экземпляр кастомного виджета дерева
        self.customDirectoryBar = CustomTreeWidget(self)

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

        # Инициализация переменных
        self.project_registry_file = "project_registry.json"
        self.project_directory = None

        # Скрываем все виджеты, которые не должны быть видимы при старте
        # self.hide_other_widgets()

    def setup_project_ui(self, project_path):
        self.project_directory = project_path
        self.stackedWidget.hide()
        self.load_directory_structure(project_path)
        self.show_other_widgets()
############################################################################
    def load_class_colors(self):
        self.directory_manager.load_class_colors_()

    def load_directory_structure(self, path):
        self.customDirectoryBar.clear()  # Очистка предыдущих элементов
        self.populate_tree_widget(self.customDirectoryBar, path)

    def load_projects_to_ui(self, projects):
        # Эта функция должна вызываться каждый раз, когда нужно обновить список проектов в UI
        # Например, после добавления нового проекта или при открытии окна выбора проекта
        if projects:
            self.projects = projects  # Сохраняем список проектов
        else:
            self.projects = []

    def load_annotations(self, label_path):
        annotations = self.directory_manager.load_annotations_(label_path)
        return annotations
    def add_resources_to_project(self, files):
        self.directory_manager.add_resources_to_project_(files)

    def update_project_registry(self, new_project_path):
        self.directory_manager.update_project_registry_(new_project_path)

    def save_class_changes_to_project_file(self):
        project_data_path = os.path.join(self.project_directory, 'project_data.json')
        if os.path.exists(project_data_path):
            with open(project_data_path, 'r') as file:
                project_data = json.load(file)
        else:
            project_data = {}

        # Обновление данных о классах в project_data
        project_data['classes'] = {class_name: color.name() for class_name, color in self.class_colors.items()}

        # Запись обновлений в файл
        with open(project_data_path, 'w') as file:
            json.dump(project_data, file, indent=4)
############################################################################
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

    # def rename_class(self):
    #     current_item = self.listWidget.currentItem()
    #     if current_item:
    #         current_class_name = current_item.text()
    #         new_class_name, ok = QInputDialog.getText(self, "Rename Class", "Enter new class name:",
    #                                                   text=current_class_name)
    #         if ok and new_class_name:
    #             color = QColorDialog.getColor(self.class_colors[current_class_name], self)
    #             if color.isValid():
    #                 self.class_colors[new_class_name] = color
    #                 if current_class_name != new_class_name:
    #                     del self.class_colors[current_class_name]
    #
    #                 # Обновляем отображение в UI
    #                 current_item.setText(new_class_name)
    #                 current_item.setBackground(color)
    #
    #                 # Сохраняем изменения в файл проекта
    #                 self.save_class_changes_to_project_file()

############################################################################
    def populate_tree_widget(self, tree_widget, directory, parent_item=None):
        self.directory_manager.populate_tree_widget_(tree_widget, directory, parent_item=None)

    def reset_ui_to_initial_state(self):
        # Метод для сброса UI к начальному состоянию
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.show()  # Показываем стек виджет
        self.hide_other_widgets()  # Скрываем остальные виджеты

    def resizeEvent(self, event):
        self.backgroundLabel.resize(self.size())
        super(MyApplication, self).resizeEvent(event)

    def display_photo(self, file_path):
        self.directory_manager.display_photo_(file_path)
        # Загрузка и отображение изображения
        pixmap = QPixmap(file_path)
        self.photo_widget.setPixmap(pixmap)
        self.photo_widget.reset_view()  # Сбросить вид при загрузке нового изображения
        self.stackedWidget.setCurrentIndex(self.stackedWidget.indexOf(self.photo_page))
        self.stackedWidget.show()# перенести по хорошкму надо
############################################################################

    def open_project(self, project_path):
        # Здесь код для открытия проекта
        print(f"Opening project at {project_path}")

    ############################################################################