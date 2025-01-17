# GUI.py
import json
import os
import shutil
import sys

from PySide6.QtCore import QDir
from PySide6.QtGui import QPixmap, QPalette, Qt, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QTreeWidgetItem, QMessageBox, \
    QTreeWidget, QColorDialog
from ui_autoannt import Ui_MainWindow, BackgroundLabel, CustomTreeWidget  # Импортируем сгенерированный класс интерфейса


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()

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

    def load_class_colors(self):
        project_data_path = os.path.join(self.project_directory, 'project_data.json')
        if os.path.exists(project_data_path):
            with open(project_data_path, 'r') as file:
                project_data = json.load(file)
                class_colors = project_data.get('classes', {})
                for class_name, color in class_colors.items():
                    self.class_colors[class_name] = QColor(color)
        else:
            # Если файла нет, предполагаем, что классы еще не созданы
            self.class_colors = {}
    def resizeEvent(self, event):
        # Обновляем размер фона при изменении размера окна
        self.backgroundLabel.resize(self.size())
        super(MyApplication, self).resizeEvent(event)

    def add_resources_to_project(self, files):
        video_dir = os.path.join(self.project_directory, 'source_video')
        photo_dir = os.path.join(self.project_directory, 'source_photo')
        dataset_dir = os.path.join(self.project_directory, 'source_datasets')

        # Создание директорий, если они не существуют
        os.makedirs(video_dir, exist_ok=True)
        os.makedirs(photo_dir, exist_ok=True)
        os.makedirs(dataset_dir, exist_ok=True)

        for file_path in files:
            if os.path.isdir(file_path):
                # Проверка наличия подпапок 'images' и 'labels'
                subfolders = [name for name in os.listdir(file_path) if os.path.isdir(os.path.join(file_path, name))]
                if 'images' in subfolders and 'labels' in subfolders:
                    # Копирование директории в source_datasets
                    shutil.copytree(file_path, os.path.join(dataset_dir, os.path.basename(file_path)))
                else:
                    # Копирование директории в корень проекта
                    shutil.copytree(file_path, os.path.join(self.project_directory, os.path.basename(file_path)))
            elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
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


    # def display_photo(self, file_path):
    #     self.stackedWidget.setCurrentIndex(self.stackedWidget.indexOf(self.photo_page))
    #     pixmap = QPixmap(file_path)
    #     self.photo_widget.setPixmap(
    #          pixmap.scaled(self.photo_widget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    #     self.stackedWidget.show()
    def load_annotations(self, label_path):
        annotations = []
        if os.path.exists(label_path):
            with open(label_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        class_id, x_center, y_center, width, height = map(float, parts)
                        annotations.append((class_id, x_center, y_center, width, height))
        return annotations

    def display_photo(self, file_path):
        # Определяем путь к директории и имя файла
        directory_path = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)

        # Проверяем, находится ли изображение в папке 'images'
        if os.path.basename(directory_path) == 'images':
            # Проверяем, существует ли родительская папка 'labels'
            parent_directory = os.path.dirname(directory_path)
            labels_path = os.path.join(parent_directory, 'labels',
                                       base_name.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg',
                                                                                                         '.txt'))

            if os.path.exists(labels_path):
                # Если файл аннотаций существует, загружаем аннотации
                annotations = self.load_annotations(labels_path)
                self.photo_widget.set_annotations(annotations)
                self.display_classes_in_bar(annotations)
            else:
                # Если файл аннотаций не найден, отображаем изображение без рамок
                self.photo_widget.set_annotations([])
        else:
            # Если папка не 'images', отображаем изображение без рамок
            self.photo_widget.set_annotations([])

        # Загрузка и отображение изображения
        pixmap = QPixmap(file_path)
        self.photo_widget.setPixmap(pixmap)
        self.photo_widget.reset_view()  # Сбросить вид при загрузке нового изображения
        self.stackedWidget.setCurrentIndex(self.stackedWidget.indexOf(self.photo_page))
        self.stackedWidget.show()

    def rename_class(self):
        current_item = self.listWidget.currentItem()
        if current_item:
            current_class_name = current_item.text()
            new_class_name, ok = QInputDialog.getText(self, "Rename Class", "Enter new class name:",
                                                      text=current_class_name)
            if ok and new_class_name:
                color = QColorDialog.getColor(self.class_colors[current_class_name], self)
                if color.isValid():
                    self.class_colors[new_class_name] = color
                    if current_class_name != new_class_name:
                        del self.class_colors[current_class_name]

                    # Обновляем отображение в UI
                    current_item.setText(new_class_name)
                    current_item.setBackground(color)

                    # Сохраняем изменения в файл проекта
                    self.save_class_changes_to_project_file()

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
    # def rename_class(self):
    #     # Получение текущего выбранного элемента в listWidget
    #     current_item = self.listWidget.currentItem()
    #     if current_item:
    #         current_class_name = current_item.text()
    #         new_class_name, ok = QInputDialog.getText(self, "Rename Class", "Enter new class name:",
    #                                                   text=current_class_name)
    #         if ok and new_class_name:
    #             color = QColorDialog.getColor(self.class_colors[current_class_name], self)
    #             if color.isValid():
    #                 # Обновление имени и цвета класса в интерфейсе
    #                 self.class_colors[new_class_name] = color
    #                 current_item.setText(new_class_name)
    #                 current_item.setBackground(color)
    #
    #                 # Если старое имя класса отличается, удаляем старый ключ
    #                 if current_class_name != new_class_name:
    #                     del self.class_colors[current_class_name]
    #
    #                 # Сохранение изменений в файле проекта
    #                 self.save_class_changes_to_project_file(new_class_name, color)
    #
    # # Функция для сохранения изменений класса в файле проекта
    # def save_class_changes_to_project_file(self, class_name, color):
    #     project_data_path = os.path.join(self.project_directory, 'project_data.json')
    #     try:
    #         # Чтение существующих данных проекта
    #         if os.path.exists(project_data_path):
    #             with open(project_data_path, 'r') as file:
    #                 project_data = json.load(file)
    #         else:
    #             project_data = {}
    #
    #         # Обновление информации о классах
    #         project_data['classes'] = project_data.get('classes', {})
    #         project_data['classes'][class_name] = color.name()  # Сохраняем имя цвета в виде строки
    #
    #         # Запись обновленных данных в файл
    #         with open(project_data_path, 'w') as file:
    #             json.dump(project_data, file, indent=4)
    #
    #         print(f"Class {class_name} updated in project file.")
    #     except Exception as e:
    #         print(f"Error updating project file: {e}")
    def open_project(self, project_path):
        # Здесь код для открытия проекта
        print(f"Opening project at {project_path}")
        # Обновление интерфейса или другие действия с проектом