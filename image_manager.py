import random

from PySide6.QtCore import QPoint, Qt, QRectF
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QLabel
from directory_manager import generate_unique_color

class ZoomableLabel(QLabel):
    def __init__(self, directory_manager, parent=None):
        super().__init__(parent)
        self.directory_manager = directory_manager
        self.annotations = []
        self.setMouseTracking(True)
        self.scale_factor = 1.0
        self.pixmap_original = None
        self.dragging = False
        self.last_mouse_position = QPoint(0, 0)
        self.offset = QPoint(0, 0)
        self.current_pos = None  # Инициализируем переменную для хранения текущей позиции курсора
        self.setMouseTracking(True)  # Включаем отслеживание курсора

    def leaveEvent(self, event):
        self.current_pos = None  # Сбрасываем положение курсора при выходе из области
        self.update()  # Перерисовка для удаления линий
    def setPixmap(self, pixmap):
            self.pixmap_original = pixmap
            if pixmap:
                    self.reset_view()
                    # Удалено: self.update_scaled_pixmap() - Не нужно обновлять масштабированное изображение здесь

    def reset_view(self):
        self.scale_factor = 1.0
        self.offset = QPoint(0, 0)

    def update_scaled_pixmap(self):
        if self.pixmap_original and not self.pixmap_original.isNull():
            width = self.pixmap_original.width() * self.scale_factor
            height = self.pixmap_original.height() * self.scale_factor
            if width > 0 and height > 0:
                scaled_pixmap = self.pixmap_original.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                super().setPixmap(scaled_pixmap)

    def wheelEvent(self, event):
            if self.pixmap_original:
                    # Расчет изменения масштаба на основе колеса прокрутки
                    scale_factor_change = 1.1 if event.angleDelta().y() > 0 else 0.9

                    # Текущее положение курсора относительно центра изображения
                    cursor_pos = event.position().toPoint()
                    relative_pos = cursor_pos - self.offset

                    # Вычисление положения курсора относительно изображения перед масштабированием
                    relative_pos_before_scale = QPoint(
                            (relative_pos.x() - self.width() / 2) / self.scale_factor,
                            (relative_pos.y() - self.height() / 2) / self.scale_factor
                    )

                    # Применяем изменение масштаба
                    self.scale_factor *= scale_factor_change

                    # Вычисление положения курсора относительно изображения после масштабирования
                    relative_pos_after_scale = QPoint(
                            relative_pos_before_scale.x() * scale_factor_change,
                            relative_pos_before_scale.y() * scale_factor_change
                    )

                    # Вычисление нового смещения так, чтобы курсор оставался на месте относительно изображения
                    self.offset = QPoint(
                            cursor_pos.x() - relative_pos_after_scale.x() * self.scale_factor - self.width() / 2,
                            cursor_pos.y() - relative_pos_after_scale.y() * self.scale_factor - self.height() / 2
                    )

                    self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.last_mouse_position = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self.window().annotation_tool_active:
            self.current_pos = event.pos()  # Обновляем текущую позицию курсора
            self.update()  # Запрашиваем перерисовку виджета
        if self.dragging:
            delta = event.position().toPoint() - self.last_mouse_position
            self.offset += delta
            self.last_mouse_position = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def set_annotations(self, annotations):
        self.annotations = annotations
        self.update()

    def paintEvent(self, event):
            super().paintEvent(event)
            painter = QPainter(self)
            if self.pixmap_original and not self.pixmap_original.isNull():
                    # Расчет размеров масштабированного изображения
                    scaled_width = self.pixmap_original.width() * self.scale_factor
                    scaled_height = self.pixmap_original.height() * self.scale_factor
                    scaled_pixmap = self.pixmap_original.scaled(scaled_width, scaled_height, Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation)

                    # Вычисление положения изображения для его центрирования
                    point = QPoint((self.width() - scaled_width) / 2, (self.height() - scaled_height) / 2) + self.offset

                    # Рисование масштабированного изображения
                    painter.drawPixmap(point, scaled_pixmap)

                    # Рисование аннотаций
                    if self.annotations:
                            for class_name, x_center, y_center, width, height in self.annotations:
                                    # Получаем цвет для класса, или красный по умолчанию
                                    color = self.directory_manager.class_colors.get(str(class_name), QColor(255, 0, 0))
                                    painter.setPen(QPen(color, 2))
                                    # Преобразование координат YOLO в QRect, учитывая масштаб и смещение
                                    x = (x_center - width / 2) * scaled_width + point.x()
                                    y = (y_center - height / 2) * scaled_height + point.y()
                                    rect_width = width * scaled_width
                                    rect_height = height * scaled_height
                                    painter.drawRect(QRectF(x, y, rect_width, rect_height))
            if self.window().annotation_tool_active and self.current_pos:
                # painter = QPainter(self)
                # Настройка и рисование белой линии
                white_pen = QPen(Qt.white, 3, Qt.SolidLine)
                painter.setPen(white_pen)
                painter.drawLine(QPoint(0, self.current_pos.y()), QPoint(self.width(), self.current_pos.y()))
                painter.drawLine(QPoint(self.current_pos.x(), 0), QPoint(self.current_pos.x(), self.height()))

                # Настройка и рисование пунктирной чёрной линии
                dash_pen = QPen(Qt.black, 1, Qt.DashLine)
                painter.setPen(dash_pen)
                painter.drawLine(QPoint(0, self.current_pos.y()), QPoint(self.width(), self.current_pos.y()))
                painter.drawLine(QPoint(self.current_pos.x(), 0), QPoint(self.current_pos.x(), self.height()))