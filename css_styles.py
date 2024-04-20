mac = """QWidget {
    background-color: #343434; /* Тёмно-серый фон */
    color: #ffffff; /* Белый текст */
    font-size: 12pt; /* Размер шрифта для общего текста */
    border: none; /* Без границ */
}

QLabel {
    color: #ffffff; /* Белый текст */
    /* font-size: 32pt; */ /* Размер шрифта для текста в QLabel, если необходим */
    /* max-height: 20px; */ /* Максимальная высота для QLabel, если необходима */
}

QPushButton {
    background-color: #5c5c5c; /* Серый фон для кнопок */
    font-size: 12pt; /* Размер шрифта для кнопок */
    border-radius: 4px; /* Скругление углов */
    padding: 6px 12px; /* Внутренние отступы */
}

QPushButton:hover {
    background-color: #757575; /* Светло-серый фон для кнопок при наведении */
}

QPushButton:pressed {
    background-color: #484848; /* Тёмно-серый фон для кнопок при нажатии */
}

QListView {
    background-color: #262626; /* Фон для компонента списка */
    border-radius: 4px; /* Скругление углов */
}

QListView::item {
    color: #ffffff; /* Белый текст для элементов списка */
    margin: 4px; /* Отступы вокруг элементов списка */
}

QListView::item:selected {
    background-color: #0066cc; /* Фон для выбранного элемента списка */
}

QScrollBar:vertical {
    width: 12px; /* Ширина вертикального скроллбара */
}

QScrollBar::handle:vertical {
    background-color: #5c5c5c; /* Фон для ползунка скроллбара */
    border-radius: 4px; /* Скругление углов ползунка */
}

QScrollBar::handle:vertical:hover {
    background-color: #757575; /* Фон для ползунка при наведении */
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none; /* Убираем стандартные кнопки у скроллбара */
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    background: none; /* Убираем стрелки у скроллбара */
}
"""

beta = """QWidget {
    background: none;
    background-color: rgba(0, 0, 0, 0);
    font-weight: bold;
    font-size: 24pt;
    color: rgb(193, 197, 189);
    border-radius: 20px;
    text-align: left;
}

QLabel {
    background-color: rgba(0, 0, 0, 0);
    color: rgb(44, 46, 38);
    font-size: 32pt;
    max-height: 39px;
}

QPushButton:hover {
    color: rgb(44, 46, 38);
}

QPushButton:pressed {
    color: rgb(136, 137, 129);
}

QPushButton {
    background-color: rgba(0, 0, 0, 0);
    height: 29px;
}
"""