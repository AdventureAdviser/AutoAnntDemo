import json
import os
import shutil

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox


class DirectoryManager:
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def add_resources_to_project_(self, files):
        app = self.app_instance
        video_dir = os.path.join(app.project_directory, 'source_video')
        photo_dir = os.path.join(app.project_directory, 'source_photo')
        dataset_dir = os.path.join(app.project_directory, 'source_datasets')

        # Создание директорий, если они не существуют
        os.makedirs(video_dir, exist_ok=True)
        os.makedirs(photo_dir, exist_ok=True)
        os.makedirs(dataset_dir, exist_ok=True)

        for file_path in files:
            if os.path.isdir(file_path):
                #    Проверка наличия подпапок 'images' и 'labels'
                subfolders = [name for name in os.listdir(file_path) if os.path.isdir(os.path.join(file_path, name))]
                if 'images' in subfolders and 'labels' in subfolders:
                    # Копирование директории в source_datasets
                    shutil.copytree(file_path, os.path.join(dataset_dir, os.path.basename(file_path)))
                else:
                    # Копирование директории в корень проекта
                    shutil.copytree(file_path, os.path.join(app.project_directory, os.path.basename(file_path)))
            elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Копирование фотографий
                shutil.copy(file_path, photo_dir)
            elif file_path.lower().endswith(('.mp4', '.avi')):
                # Копирование видео
                shutil.copy(file_path, video_dir)

        # Обновление дерева директорий после добавления файлов
        app.load_directory_structure(app.project_directory)
        QMessageBox.information(app, "Resources Added", "Resources have been successfully added to the project.")

    def update_project_registry_(self, new_project_path):
        app = self.app_instance
        # Чтение существующих данных
        try:
            with open(app.project_registry_file, 'r') as file:
                try:
                    projects = json.load(file)
                except json.JSONDecodeError:
                    projects = []  # Если файл пуст или данные некорректны, используем пустой список
        except FileNotFoundError:
            projects = []

        # Добавление нового проекта
        if new_project_path not in projects:
            projects.append(new_project_path)
            with open(app.project_registry_file, 'w') as file:
                json.dump(projects, file, indent=4)  # Форматированный вывод для удобства
            print(f"Project {new_project_path} added to registry.")

        app.load_projects_to_ui(projects)  # Обновление UI с доступными проектами

    def populate_tree_widget_(self, tree_widget, directory, parent_item=None):
        if parent_item is None:
            parent_item = tree_widget.invisibleRootItem()
        for item in sorted(os.listdir(directory)):
            child_item = QTreeWidgetItem(parent_item, [item])
            child_path = os.path.join(directory, item)
            if os.path.isdir(child_path):
                self.populate_tree_widget_(tree_widget, child_path, child_item)
            else:
                child_item.setExpanded(False)  # Устанавливаем элементы не раскрытыми

    def load_class_colors_(self):
        app = self.app_instance
        project_data_path = os.path.join(app.project_directory, 'project_data.json')
        if os.path.exists(project_data_path):
            with open(project_data_path, 'r') as file:
                project_data = json.load(file)
                class_colors = project_data.get('classes', {})
                for class_name, color in class_colors.items():
                    app.class_colors[class_name] = QColor(color)
        else:
            # Если файла нет, предполагаем, что классы еще не созданы
            app.class_colors = {}

    def load_annotations_(self, label_path):
        annotations = []
        if os.path.exists(label_path):
            with open(label_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        class_id, x_center, y_center, width, height = map(float, parts)
                        annotations.append((class_id, x_center, y_center, width, height))
        return annotations

    def display_photo_(self, file_path):
        app = self.app_instance
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
                annotations = app.load_annotations(labels_path)
                app.photo_widget.set_annotations(annotations)
                app.display_classes_in_bar(annotations)
            else:
                # Если файл аннотаций не найден, отображаем изображение без рамок
                app.photo_widget.set_annotations([])
        else:
            # Если папка не 'images', отображаем изображение без рамок
            app.photo_widget.set_annotations([])