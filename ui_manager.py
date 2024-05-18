import json
import os

from PySide6.QtGui import QPixmap, QColor, Qt, QCursor
from PySide6.QtWidgets import QMainWindow, QFileDialog, QInputDialog, QColorDialog, QMessageBox, QListWidgetItem
from ui import Ui_MainWindow, BackgroundLabel, CustomTreeWidget
from directory_manager import DirectoryManager, generate_unique_color


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.customDirectoryBar = CustomTreeWidget(parent=self, directory_manager=self.directory_manager)

        self.setupUi(self)

        self.backgroundLabel = BackgroundLabel(self)
        self.backgroundLabel.lower()
        self.backgroundLabel.resize(self.size())
        self.backgroundLabel.show()

        self.stackedWidget.setCurrentIndex(0)

        self.new_pushButton.clicked.connect(self.onNewProjectClicked)
        self.prodgect_pushButton.clicked.connect(self.reset_ui_to_initial_state)
        self.choose_pushButton.clicked.connect(self.onChooseProjectClicked)
        self.create_pushButton_2.clicked.connect(self.activate_annotation_tool)
        self.annotation_tool_active = False

    def activate_annotation_tool(self):
        if self.listWidget.currentItem() is None:
            QMessageBox.warning(self, "Select a Class", "Please select a class before creating an annotation.")
        else:
            self.annotation_tool_active = True  # Включаем флаг активации
            self.photo_widget.setCursor(QCursor(Qt.CrossCursor))  # Устанавливаем курсор для photo_widget

    def deactivate_annotation_tool(self):
        self.annotation_tool_active = False  # Выключаем флаг активации
        self.photo_widget.unsetCursor()  # Сбрасываем курсор для photo_widget
    def setup_project_ui(self, project_path):
        self.directory_manager.project_directory = project_path
        self.stackedWidget.hide()
        self.load_directory_structure(project_path)
        self.show_other_widgets()
    def add_resources_to_project(self, files):
        self.directory_manager.add_resources_to_project_(files)#относится к treewidget
        self.load_directory_structure(self.directory_manager.project_directory)
        QMessageBox.information(self, "Resources Added", "Resources have been successfully added to the project.")

    def load_directory_structure(self, path):
        self.customDirectoryBar.clear()  # Очистка предыдущих элементов
        self.populate_tree_widget(self.customDirectoryBar, path)

    def onNewProjectClicked(self):
        project_folder = QFileDialog.getExistingDirectory(self, "Select Project Folder")
        if project_folder:
            self.load_directory_structure(project_folder)
            project_name, ok = QInputDialog.getText(self, "Project Name", "Enter the name of the new project:")
            project_path = self.directory_manager.create_new_project(project_folder, ok, project_name)
            if project_path:
                self.directory_manager.update_project_registry(project_path)
                self.setup_project_ui(project_path)
    def onChooseProjectClicked(self):
        self.directory_manager.projects_list()
        if self.directory_manager.projects:
            project, ok = QInputDialog.getItem(self, "Select a Project", "Choose a project:", self.directory_manager.projects, 0, False)
            if ok and project:
                self.setup_project_ui(project)
        else:
            print("No projects found. Please create a new project first.")

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
        annotations = self.directory_manager.display_photo_(file_path)
        # Получаем путь датасета из пути изображения
        data_set = self.directory_manager.get_dataset_from_image_path(file_path)
        # Загрузка и отображение изображения
        if annotations:
            self.photo_widget.set_annotations(annotations)
            # Передаем аннотации и датасет в метод для отображения классов
            if data_set:
                self.display_classes_in_bar(annotations, data_set)
            else:
                print("Failed to identify dataset from image path.")
        else:
            # Если файл аннотаций не найден, отображаем изображение без рамок
            self.photo_widget.set_annotations([])

        pixmap = QPixmap(file_path)
        self.photo_widget.setPixmap(pixmap)
        self.photo_widget.reset_view()  # Сбросить вид при загрузке нового изображения
        self.stackedWidget.setCurrentIndex(self.stackedWidget.indexOf(self.photo_page))
        self.stackedWidget.show()

    def show_other_widgets(self):
        # Показываем виджеты, связанные с проектом
        self.ClassesBar.show()
        self.AnntBar.show()
        self.NeuralBar.show()
        self.ModelBar.show()
        self.customDirectoryBar.show()
        # self.VideoSroll.show()
        self.ProdgectBar.show()

    def hide_other_widgets(self):
        # Скрытие всех виджетов кроме стек виджета
        self.ClassesBar.hide()
        self.AnntBar.hide()
        self.NeuralBar.hide()
        self.ModelBar.hide()
        self.customDirectoryBar.hide()
        self.VideoSroll.hide()
        self.ProdgectBar.hide()

############################################################################
    # def update_annotations_display(self, file_path):
    #     self.photo_widget.update()

    def rename_class(self):
        current_item = self.listWidget.currentItem()
        if current_item:
            current_class_id = current_item.data(Qt.UserRole)  # Предполагаем, что ID класса сохранён как user data
            current_class_name = current_item.text()
            new_class_name, ok = QInputDialog.getText(self, "Rename Class", "Enter new class name:",
                                                      text=current_class_name)
            if ok and new_class_name and new_class_name != current_class_name:
                # Проверка на наличие класса с таким же именем в списке
                if any(new_class_name == self.listWidget.item(i).text() for i in range(self.listWidget.count())):
                    QMessageBox.warning(self, "Rename Class", "A class with this name already exists.")
                    return
                print(self.directory_manager.class_colors)
                color = QColorDialog.getColor(QColor(self.directory_manager.class_colors[current_class_id]), self)
                if color.isValid():
                    data_set = self.directory_manager.current_dataset  # Предполагаем, что current_dataset хранит текущий датасет
                    self.directory_manager.save_class_changes_to_project_file(current_class_id, new_class_name, color, data_set)
                    current_item.setText(new_class_name)
                    current_item.setBackground(color)
                    self.listWidget.repaint()  # Обновляем listWidget для отображения изменений
                    self.display_photo(self.directory_manager.current_image_path)
                    self.photo_widget.update()
                    # self.update_annotations_display(self.directory_manager.current_image_path)
        else:
            QMessageBox.information(self, "Rename Class", "Please select a class to rename.")

    def display_classes_in_bar(self, annotations, data_set):
        self.directory_manager.load_class_colors_(data_set)
        self.listWidget.clear()
        self.directory_manager.load_class_colors_(self.directory_manager.current_dataset)
        class_ids = set(ann[0] for ann in annotations)  # Извлечение ID классов из аннотаций

        # Загрузка классов из текущего датасета
        classes = self.directory_manager.load_classes_from_dataset(data_set)

        for class_id in class_ids:
            class_id = str(class_id)  # Убедимся, что class_id - это строка
            if class_id not in classes:
                # Если класса нет, генерируем уникальный цвет и добавляем его
                color = generate_unique_color([QColor(cls['color']) for cls in classes.values()])
                classes[class_id] = {
                    "id": class_id,
                    "class": f"Class_{class_id}",
                    "color": color.name()
                }
                # Сохраняем новый класс в файле проекта
                self.directory_manager.save_class_changes_to_project_file(class_id, f"Class_{class_id}", color,
                                                                          data_set)

            class_info = classes[class_id]
            class_name = class_info['class']
            color = QColor(class_info['color'])
            item = QListWidgetItem(class_name)
            item.setBackground(color)
            item.setData(Qt.UserRole, class_id)
            self.listWidget.addItem(item)

    # def add_class_to_bar(self, class_name, color):
    #         # Приведем class_name к строке, чтобы избежать ошибок типизации
    #         class_name = str(class_name)
    #         item = QListWidgetItem(class_name)
    #         item.setBackground(color)
    #         item.setData(Qt.UserRole, class_id)
    #         self.listWidget.addItem(item)