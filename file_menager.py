# from PySide6.QtWidgets import (
#     QDialog, QVBoxLayout, QHBoxLayout, QColumnView, QFileSystemModel,
#     QPushButton, QFrame, QApplication
# )
# from PySide6.QtCore import QDir, Qt, QSize
# from PySide6.QtGui import QStandardItemModel, QStandardItem
#
# class CustomFileDialog(QDialog):
#     def __init__(self, parent=None):
#         super(CustomFileDialog, self).__init__(parent)
#         self.setWindowTitle("Select Resources")
#         self.setGeometry(100, 100, 800, 600)
#         self.selected_files = []
#
#         # Инициализация модели файловой системы
#         self.fileSystemModel = QFileSystemModel()
#         self.fileSystemModel.setRootPath(QDir.homePath())
#
#         # Инициализация QColumnView
#         self.columnView = QColumnView()
#         self.columnView.setModel(self.fileSystemModel)
#         self.columnView.setRootIndex(self.fileSystemModel.index(QDir.homePath()))
#
#         # Компоновка для QColumnView
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.columnView)
#
#         # Кнопка "Назад"
#         backButton = QPushButton("Back")
#         backButton.clicked.connect(self.navigate_back)
#
#         # Кнопка "Добавить"
#         addButton = QPushButton("Add")
#         addButton.clicked.connect(self.add_selected)
#
#         # Кнопка "Отмена"
#         cancelButton = QPushButton("Cancel")
#         cancelButton.clicked.connect(self.reject)
#
#         # Кнопка "OK"
#         okButton = QPushButton("OK")
#         okButton.clicked.connect(self.accept_selection)
#
#         # Компоновка для кнопок
#         buttonLayout = QHBoxLayout()
#         buttonLayout.addWidget(backButton)
#         buttonLayout.addWidget(addButton)
#         buttonLayout.addStretch()
#         buttonLayout.addWidget(cancelButton)
#         buttonLayout.addWidget(okButton)
#
#         # Добавление компоновки для кнопок в главную компоновку
#         layout.addLayout(buttonLayout)
#
#     def navigate_back(self):
#         # Вернуться на уровень выше
#         current = self.columnView.rootIndex()
#         self.columnView.setRootIndex(current.parent())
#
#     def add_selected(self):
#         # Добавить текущий выбранный элемент
#         index = self.columnView.currentIndex()
#         if index.isValid():
#             file_path = self.fileSystemModel.filePath(index)
#             # Добавляем только файлы, а не директории
#             if not self.fileSystemModel.isDir(index):
#                 self.selected_files.append(file_path)
#
#     def accept_selection(self):
#         # Принять выбранные файлы и закрыть диалог
#         self.accept()
#
#     def exec_(self):
#         result = super(CustomFileDialog, self).exec_()
#         if result == QDialog.Accepted:
#             return self.selected_files
#         else:
#             return []
import os

# from PySide6.QtWidgets import (
#     QDialog, QVBoxLayout, QHBoxLayout, QColumnView, QFileSystemModel,
#     QPushButton, QApplication, QFileDialog
# )
# from PySide6.QtCore import QDir, Qt
# from PySide6.QtGui import QStandardItemModel, QStandardItem
#
# class CustomFileDialog(QDialog):
#     def __init__(self, parent=None):
#         super(CustomFileDialog, self).__init__(parent)
#         self.setWindowTitle("Select Resources")
#         self.setGeometry(100, 100, 800, 600)
#         self.selected_files = []
#         self.history_stack = []  # Стек для истории переходов
#
#         # Инициализация модели файловой системы
#         self.fileSystemModel = QFileSystemModel()
#         self.fileSystemModel.setRootPath(QDir.homePath())
#         self.fileSystemModel.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries)
#
#         # Инициализация QColumnView
#         self.columnView = QColumnView()
#         self.columnView.setModel(self.fileSystemModel)
#         self.set_initial_root()
#
#         # Компоновка для QColumnView
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.columnView)
#
#         # Кнопка "Назад"
#         backButton = QPushButton("Back")
#         backButton.clicked.connect(self.navigate_back)
#
#         # Кнопка "Добавить"
#         addButton = QPushButton("Add")
#         addButton.clicked.connect(self.add_selected)
#
#         # Кнопка "Отмена"
#         cancelButton = QPushButton("Cancel")
#         cancelButton.clicked.connect(self.reject)
#
#         # Кнопка "OK"
#         okButton = QPushButton("OK")
#         okButton.clicked.connect(self.accept_selection)
#
#         # Компоновка для кнопок
#         buttonLayout = QHBoxLayout()
#         buttonLayout.addWidget(backButton)
#         buttonLayout.addWidget(addButton)
#         buttonLayout.addStretch()
#         buttonLayout.addWidget(cancelButton)
#         buttonLayout.addWidget(okButton)
#
#         # Добавление компоновки для кнопок в главную компоновку
#         layout.addLayout(buttonLayout)
#
#     def set_initial_root(self):
#         initial_index = self.fileSystemModel.index(QDir.homePath())
#         self.columnView.setRootIndex(initial_index)
#         self.history_stack.append(initial_index)
#         # Можно явно очистить выбор после установки корневого индекса
#         self.columnView.clearSelection()
#
#     def navigate_back(self):
#         if len(self.history_stack) > 1:
#             self.history_stack.pop()  # Удаляем текущий индекс
#             new_index = self.history_stack[-1]
#             self.columnView.clearSelection()  # Сбросить текущее выделение
#             self.columnView.setRootIndex(new_index)
#
#     def add_selected(self):
#         indexes = self.columnView.selectedIndexes()
#         # Очищаем предыдущий выбор, если это новая операция выбора
#         if not indexes:
#             self.selected_files.clear()
#
#         for index in indexes:
#             if index.column() == 0:  # Учитываем только элементы из первой колонки
#                 file_path = self.fileSystemModel.filePath(index)
#                 if not self.fileSystemModel.isDir(index) or file_path not in self.selected_files:
#                     self.selected_files.append(file_path)
#
#         # Возможно, потребуется вызов метода для обновления UI или дальнейшей обработки списка файлов
#
#     def accept_selection(self):
#         self.accept()
#
#     def exec_(self):
#         result = super(CustomFileDialog, self).exec_()
#         if result == QDialog.Accepted:
#             return self.selected_files
#         else:
#             return []
#
#     # ... Остальные методы класса ...
from PySide6.QtWidgets import QFileSystemModel, QColumnView, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QApplication
from PySide6.QtCore import QDir, Qt

class CustomFileDialog(QDialog):
    def __init__(self, parent=None):
        super(CustomFileDialog, self).__init__(parent)
        self.setWindowTitle("Select Resources")
        # self.setObjectName(u"Directory")
        self.setGeometry(100, 100, 800, 600)
        self.selected_files = []

        # Инициализация модели файловой системы
        self.fileSystemModel = QFileSystemModel(self)
        self.fileSystemModel.setRootPath(QDir.homePath())

        # Инициализация QColumnView
        self.columnView = QColumnView(self)
        self.columnView.setModel(self.fileSystemModel)
        self.columnView.clearSelection()
        self.set_initial_root(QDir.homePath())

        # Компоновка для QColumnView
        columnLayout = QVBoxLayout()
        columnLayout.addWidget(self.columnView)

        # Кнопка "Добавить"
        self.addButton = QPushButton("Add", self)
        self.addButton.clicked.connect(self.add_selected)

        # Кнопка "Отмена"
        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.clicked.connect(self.reject)

        # Кнопка "OK"
        self.okButton = QPushButton("OK", self)
        self.okButton.clicked.connect(self.accept_selection)

        # Компоновка для кнопок
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.okButton)

        # Объединение компоновок
        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(columnLayout)
        mainLayout.addLayout(buttonLayout)

    def set_initial_root(self, path):
        index = self.fileSystemModel.index(path)
        self.columnView.setRootIndex(index)
        self.columnView.clearSelection()  # Очистка выбора после установки корня

    def add_selected(self):
        selected_indexes = self.columnView.selectedIndexes()
        current_root_path = self.fileSystemModel.filePath(self.columnView.rootIndex())
        deepest_common_path = None

        # Найти самый глубокий общий путь для всех выбранных элементов
        for index in selected_indexes:
            file_path = self.fileSystemModel.filePath(index)
            if not deepest_common_path:
                deepest_common_path = file_path
            else:
                # Обрезать путь до самого глубокого общего каталога
                while not file_path.startswith(deepest_common_path):
                    deepest_common_path = deepest_common_path.rsplit(os.sep, 1)[0]

        # Если есть общий путь и он в пределах текущего корня, добавить выбранные элементы
        if deepest_common_path and deepest_common_path.startswith(current_root_path):
            for index in selected_indexes:
                file_path = self.fileSystemModel.filePath(index)
                if file_path.startswith(deepest_common_path) and file_path not in self.selected_files:
                    self.selected_files.append(file_path)
                    print(f"Added: {file_path}")  # Логирование добавленных элементов

    def accept_selection(self):
        # Принять выбранные файлы и закрыть диалог
        self.accept()

    def exec_(self):
        result = super(CustomFileDialog, self).exec_()
        return self.selected_files if result == QDialog.Accepted else []

# Тестирование диалога
if __name__ == "__main__":
    app = QApplication([])
    dialog = CustomFileDialog()
    selected_files = dialog.exec_()
    print(selected_files)




# from PySide6.QtWidgets import QFileSystemModel, QColumnView, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QFileDialog
# from PySide6.QtCore import QDir, Qt
#
# class CustomFileDialog(QDialog):
#     def __init__(self, parent=None):
#         super(CustomFileDialog, self).__init__(parent)
#         self.setWindowTitle("Select Resources")
#         self.setGeometry(100, 100, 800, 600)
#         self.selected_files = []
#         self.history_stack = []
#
#         self.fileSystemModel = QFileSystemModel(self)
#         self.columnView = QColumnView(self)
#         self.columnView.setModel(self.fileSystemModel)
#         self.setup_initial_view()
#
#         self.backButton = QPushButton("Back", self)
#         self.backButton.clicked.connect(self.navigate_back)
#         self.addButton = QPushButton("Add", self)
#         self.addButton.clicked.connect(self.add_selected)
#         self.cancelButton = QPushButton("Cancel", self)
#         self.cancelButton.clicked.connect(self.reject)
#         self.okButton = QPushButton("OK", self)
#         self.okButton.clicked.connect(self.accept_selection)
#
#         mainLayout = QVBoxLayout(self)
#         mainLayout.addWidget(self.columnView)
#         buttonLayout = QHBoxLayout()
#         buttonLayout.addWidget(self.backButton)
#         buttonLayout.addWidget(self.addButton)
#         buttonLayout.addStretch()
#         buttonLayout.addWidget(self.cancelButton)
#         buttonLayout.addWidget(self.okButton)
#         mainLayout.addLayout(buttonLayout)
#
#     def setup_initial_view(self):
#         initialPath = QDir.homePath()  # или другой путь, который вы предпочитаете
#         self.fileSystemModel.setRootPath(initialPath)
#         index = self.fileSystemModel.index(initialPath)
#         self.columnView.setRootIndex(index)
#         self.history_stack = [index]
#
#     def navigate_back(self):
#         if len(self.history_stack) > 1:
#             self.history_stack.pop()
#             self.columnView.setRootIndex(self.history_stack[-1])
#             self.columnView.clearSelection()
#
#     def add_selected(self):
#         indexes = self.columnView.selectedIndexes()
#         for index in indexes:
#             file_path = self.fileSystemModel.filePath(index)
#             if self.fileSystemModel.isDir(index) and file_path not in self.selected_files:
#                 self.selected_files.append(file_path)
#
#     def accept_selection(self):
#         self.accept()
#
#     def exec_(self):
#         result = super(CustomFileDialog, self).exec_()
#         return self.selected_files if result == QDialog.Accepted else []
