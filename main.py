import sys
from PySide6.QtWidgets import QApplication
from ui_manager import MyApplication  # Импортируем класс приложения из GUI.py

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
