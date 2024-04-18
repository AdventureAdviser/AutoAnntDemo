import os
from PySide6.QtWidgets import QFileSystemModel, QColumnView, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QApplication
from PySide6.QtCore import QDir, Qt

class CustomFileDialog(QDialog):
    def __init__(self, parent=None):
        super(CustomFileDialog, self).__init__(parent)
        # # Настройка стилей
        # self.setStyleSheet("""
        #             QDialog {
        #                 background-color: #fff;
        #                 border: none;
        #             }
        #             QTreeView {
        #                 border: none;
        #             }
        #             QPushButton {
        #                 background-color: #f6f6f6;
        #                 border: none;
        #             }
        #         """)

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