import json
import os
import shutil

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTreeWidgetItem, QMessageBox
import random


def generate_unique_color(existing_colors, alpha=200):
    while True:
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), alpha)
        color_hsl = color.toHsl()
        color_hsl.setHsl(color_hsl.hue(), (color_hsl.saturation() * 0.6), color_hsl.lightness())  # Уменьшаем насыщенность
        color = color_hsl.toRgb()
        if color not in existing_colors:
            return color


class DirectoryManager:
    def __init__(self):
        self.class_colors = {}
        self.project_directory = None
        self.project_registry_file = "project_registry.json"

    def save_class_changes_to_project_file(self, class_name, color):
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

    def projects_list(self):
        if not hasattr(self, 'projects') or not self.projects:
            if os.path.exists(self.project_registry_file):
                with open(self.project_registry_file, 'r') as file:
                    try:
                        self.projects = json.load(file)
                    except json.JSONDecodeError:
                        self.projects = []
            else:
                print("No project registry file found.")
                self.projects = []

    def update_project_registry(self, new_project_path):
        self.load_projects(self.update_project_registry_(new_project_path))

    def load_projects(self, projects):
        if projects:
            self.projects = projects
        else:
            self.projects = []

    def buildFilePath(self, item):
        path = item.text(0)
        while item.parent() is not None:
            item = item.parent()
            path = os.path.join(item.text(0), path)
        return path

    def create_new_project(self, project_folder, ok, project_name):
        if ok and project_name:
            project_path = os.path.join(project_folder, project_name)
            if not os.path.exists(project_path):
                os.makedirs(project_path)
                return project_path

    def add_resources_to_project_(self, files):
        video_dir = os.path.join(self.project_directory, 'source_video')
        photo_dir = os.path.join(self.project_directory, 'source_photo')
        dataset_dir = os.path.join(self.project_directory, 'source_datasets')

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
                    shutil.copytree(file_path, os.path.join(self.project_directory, os.path.basename(file_path)))
            elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Копирование фотографий
                shutil.copy(file_path, photo_dir)
            elif file_path.lower().endswith(('.mp4', '.avi')):
                # Копирование видео
                shutil.copy(file_path, video_dir)

    def update_project_registry_(self, new_project_path):
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

        return projects

    def populate_tree_widget_(self, tree_widget, directory, parent_item=None):# отвеччает за структуру дериктории выбора ресурсов
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
                annotations = self.load_annotations_(labels_path)
                return annotations