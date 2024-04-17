
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1755, 1019)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStyleSheet(u"#MainWindow  {\n"
"    background-image: url('C:/Users/batma/OneDrive/\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0441\u0442\u043e\u043b/AutoAnnt_GUI/images/BackGroundRef_2_2.png');\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size: cover;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setToolTipDuration(-1)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background: none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"font-weight: bold;\n"
"font-size: 24pt;\n"
"color: rgb(193, 197, 189);\n"
"border-radius: 20px;\n"
"text-align: left;\n"
"}\n"
"QLabel {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(44, 46, 38);\n"
"font-size: 32pt;\n"
"with: 175px;\n"
"max-height: 39px;\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(44, 46, 38);\n"
"}\n"
"QPushButton:pressed {\n"
"color: rgb(136, 137, 129);\n"
"}\n"
"QPushButton {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"with: 175px;\n"
"height: 29px;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(30)
        self.gridLayout_5.setVerticalSpacing(25)
        self.gridLayout_5.setContentsMargins(30, 25, 30, 25)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ClassesBar = QWidget(self.centralwidget)
        self.ClassesBar.setObjectName(u"ClassesBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClassesBar.sizePolicy().hasHeightForWidth())
        self.ClassesBar.setSizePolicy(sizePolicy)
        self.ClassesBar.setMinimumSize(QSize(260, 0))
        self.ClassesBar.setStyleSheet(u"#ClassesBar {\n"
"background-color: rgba(246, 247, 240, 73);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.ClassesBar)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.class_label = QLabel(self.ClassesBar)
        self.class_label.setObjectName(u"class_label")
        self.class_label.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.class_label.sizePolicy().hasHeightForWidth())
        self.class_label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.class_label)

        self.create_pushButton = QPushButton(self.ClassesBar)
        self.create_pushButton.setObjectName(u"create_pushButton")

        self.verticalLayout.addWidget(self.create_pushButton)

        self.rename_pushButton = QPushButton(self.ClassesBar)
        self.rename_pushButton.setObjectName(u"rename_pushButton")

        self.verticalLayout.addWidget(self.rename_pushButton)

        self.delete_pushButton = QPushButton(self.ClassesBar)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.delete_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_pushButton.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.delete_pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.listWidget = QListWidget(self.ClassesBar)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy3)
        self.listWidget.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.ClassesBar)

        self.AnntBar = QWidget(self.centralwidget)
        self.AnntBar.setObjectName(u"AnntBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.AnntBar.sizePolicy().hasHeightForWidth())
        self.AnntBar.setSizePolicy(sizePolicy4)
        self.AnntBar.setMinimumSize(QSize(260, 146))
        self.AnntBar.setStyleSheet(u"#AnntBar {\n"
"background-color: rgba(246, 247, 240, 73);\n"
"min-height: 146px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.AnntBar)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.annotation_label = QLabel(self.AnntBar)
        self.annotation_label.setObjectName(u"annotation_label")
        sizePolicy1.setHeightForWidth(self.annotation_label.sizePolicy().hasHeightForWidth())
        self.annotation_label.setSizePolicy(sizePolicy1)
        self.annotation_label.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.annotation_label)

        self.create_pushButton_2 = QPushButton(self.AnntBar)
        self.create_pushButton_2.setObjectName(u"create_pushButton_2")
        self.create_pushButton_2.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.create_pushButton_2)

        self.delete_pushButton_2 = QPushButton(self.AnntBar)
        self.delete_pushButton_2.setObjectName(u"delete_pushButton_2")

        self.verticalLayout_3.addWidget(self.delete_pushButton_2)

        self.delete_pushButton_3 = QPushButton(self.AnntBar)
        self.delete_pushButton_3.setObjectName(u"delete_pushButton_3")

        self.verticalLayout_3.addWidget(self.delete_pushButton_3)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.AnntBar)

        self.NeuralBar = QWidget(self.centralwidget)
        self.NeuralBar.setObjectName(u"NeuralBar")
        sizePolicy4.setHeightForWidth(self.NeuralBar.sizePolicy().hasHeightForWidth())
        self.NeuralBar.setSizePolicy(sizePolicy4)
        self.NeuralBar.setMinimumSize(QSize(260, 146))
        self.NeuralBar.setStyleSheet(u"#NeuralBar {\n"
"background-color: rgba(246, 247, 240, 73);\n"
"min-height: 146px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.NeuralBar)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.neural_label = QLabel(self.NeuralBar)
        self.neural_label.setObjectName(u"neural_label")
        sizePolicy1.setHeightForWidth(self.neural_label.sizePolicy().hasHeightForWidth())
        self.neural_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.neural_label)

        self.auto_pushButton = QPushButton(self.NeuralBar)
        self.auto_pushButton.setObjectName(u"auto_pushButton")

        self.verticalLayout_4.addWidget(self.auto_pushButton)

        self.delete_pushButton_4 = QPushButton(self.NeuralBar)
        self.delete_pushButton_4.setObjectName(u"delete_pushButton_4")

        self.verticalLayout_4.addWidget(self.delete_pushButton_4)

        self.save_pushButton = QPushButton(self.NeuralBar)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.verticalLayout_4.addWidget(self.save_pushButton)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.NeuralBar)

        self.ModelBar = QWidget(self.centralwidget)
        self.ModelBar.setObjectName(u"ModelBar")
        sizePolicy4.setHeightForWidth(self.ModelBar.sizePolicy().hasHeightForWidth())
        self.ModelBar.setSizePolicy(sizePolicy4)
        self.ModelBar.setMinimumSize(QSize(260, 146))
        self.ModelBar.setStyleSheet(u"#ModelBar {\n"
"background-color: rgba(246, 247, 240, 73);\n"
"min-height: 146px;\n"
"}")
        self.gridLayout = QGridLayout(self.ModelBar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.model_icon_label = QLabel(self.ModelBar)
        self.model_icon_label.setObjectName(u"model_icon_label")
        self.model_icon_label.setMinimumSize(QSize(60, 60))
        self.model_icon_label.setMaximumSize(QSize(40, 39))
        self.model_icon_label.setPixmap(QPixmap(u":/hover/hover/account_tree.svg"))
        self.model_icon_label.setScaledContents(True)

        self.gridLayout_6.addWidget(self.model_icon_label, 1, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.model_label = QLabel(self.ModelBar)
        self.model_label.setObjectName(u"model_label")
        sizePolicy1.setHeightForWidth(self.model_label.sizePolicy().hasHeightForWidth())
        self.model_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.model_label)

        self.lineEdit = QLineEdit(self.ModelBar)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.track_pushButton = QPushButton(self.ModelBar)
        self.track_pushButton.setObjectName(u"track_pushButton")

        self.verticalLayout_5.addWidget(self.track_pushButton)

        self.save_pushButton_2 = QPushButton(self.ModelBar)
        self.save_pushButton_2.setObjectName(u"save_pushButton_2")

        self.verticalLayout_5.addWidget(self.save_pushButton_2)


        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 1, 3, 1)


        self.gridLayout.addLayout(self.gridLayout_6, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.ModelBar)


        self.gridLayout_5.addLayout(self.verticalLayout_6, 0, 0, 2, 1)

        self.DirectoryBar = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.DirectoryBar.setHeaderItem(__qtreewidgetitem)
        self.DirectoryBar.setObjectName(u"DirectoryBar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.DirectoryBar.sizePolicy().hasHeightForWidth())
        self.DirectoryBar.setSizePolicy(sizePolicy6)
        self.DirectoryBar.setMinimumSize(QSize(260, 0))
        self.DirectoryBar.setStyleSheet(u"#DirectoryBar {\n"
"background-color: rgba(246, 247, 240, 73);\n"
"}")

        self.gridLayout_5.addWidget(self.DirectoryBar, 0, 2, 2, 1)

        self.VideoSroll = QWidget(self.centralwidget)
        self.VideoSroll.setObjectName(u"VideoSroll")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.VideoSroll.sizePolicy().hasHeightForWidth())
        self.VideoSroll.setSizePolicy(sizePolicy7)
        self.VideoSroll.setMinimumSize(QSize(0, 60))
        self.VideoSroll.setStyleSheet(u"\n"
"background-color: rgba(246, 247, 240, 73);\n"
"")

        self.gridLayout_5.addWidget(self.VideoSroll, 1, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy8)
        self.stackedWidget.setStyleSheet(u"")
        self.enter_page = QWidget()
        self.enter_page.setObjectName(u"enter_page")
        self.gridLayout_9 = QGridLayout(self.enter_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer = QSpacerItem(20, 360, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(403, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.enter_page)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(16777215, 39))

        self.verticalLayout_7.addWidget(self.label)

        self.choose_pushButton = QPushButton(self.enter_page)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.verticalLayout_7.addWidget(self.choose_pushButton)

        self.new_pushButton = QPushButton(self.enter_page)
        self.new_pushButton.setObjectName(u"new_pushButton")
        self.new_pushButton.setCheckable(True)

        self.verticalLayout_7.addWidget(self.new_pushButton)


        self.gridLayout_9.addLayout(self.verticalLayout_7, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(403, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 359, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.enter_page)
        self.video_page = QWidget()
        self.video_page.setObjectName(u"video_page")
        self.video_page.setStyleSheet(u"#video_page {\n"
"background-color: rgba(246, 247, 240, 73);\n"
"}")
        self.gridLayout_10 = QGridLayout(self.video_page)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setVerticalSpacing(6)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 6)
        self.label_3 = QLabel(self.video_page)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(35)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.previous_frame_pushButton = QPushButton(self.video_page)
        self.previous_frame_pushButton.setObjectName(u"previous_frame_pushButton")
        sizePolicy4.setHeightForWidth(self.previous_frame_pushButton.sizePolicy().hasHeightForWidth())
        self.previous_frame_pushButton.setSizePolicy(sizePolicy4)
        icon = QIcon()
        icon.addFile(u":/no_active/no_active/skip_previous.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_frame_pushButton.setIcon(icon)
        self.previous_frame_pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.previous_frame_pushButton)

        self.next_frame_pushButton = QPushButton(self.video_page)
        self.next_frame_pushButton.setObjectName(u"next_frame_pushButton")
        sizePolicy4.setHeightForWidth(self.next_frame_pushButton.sizePolicy().hasHeightForWidth())
        self.next_frame_pushButton.setSizePolicy(sizePolicy4)
        icon1 = QIcon()
        icon1.addFile(u":/no_active/no_active/skip_next.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_frame_pushButton.setIcon(icon1)
        self.next_frame_pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.next_frame_pushButton)

        self.play_pushButton = QPushButton(self.video_page)
        self.play_pushButton.setObjectName(u"play_pushButton")
        sizePolicy4.setHeightForWidth(self.play_pushButton.sizePolicy().hasHeightForWidth())
        self.play_pushButton.setSizePolicy(sizePolicy4)
        self.play_pushButton.setMinimumSize(QSize(44, 0))
        icon2 = QIcon()
        icon2.addFile(u":/no_active/no_active/play_arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.play_pushButton.setIcon(icon2)
        self.play_pushButton.setIconSize(QSize(44, 55))
        self.play_pushButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.play_pushButton)

        self.screen_pushButton = QPushButton(self.video_page)
        self.screen_pushButton.setObjectName(u"screen_pushButton")
        sizePolicy4.setHeightForWidth(self.screen_pushButton.sizePolicy().hasHeightForWidth())
        self.screen_pushButton.setSizePolicy(sizePolicy4)
        self.screen_pushButton.setMinimumSize(QSize(0, 0))
        icon3 = QIcon()
        icon3.addFile(u":/no_active/no_active/screenshot_region.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.screen_pushButton.setIcon(icon3)
        self.screen_pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.screen_pushButton)

        self.neural_pushButton = QPushButton(self.video_page)
        self.neural_pushButton.setObjectName(u"neural_pushButton")
        sizePolicy4.setHeightForWidth(self.neural_pushButton.sizePolicy().hasHeightForWidth())
        self.neural_pushButton.setSizePolicy(sizePolicy4)
        icon4 = QIcon()
        icon4.addFile(u":/no_active/no_active/account_tree.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.neural_pushButton.setIcon(icon4)
        self.neural_pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.neural_pushButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.gridLayout_10.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.video_page)
        self.photo_page = QWidget()
        self.photo_page.setObjectName(u"photo_page")
        self.photo_page.setStyleSheet(u"#photo_page {\n"
"background-color: rgba(246, 247, 240, 73);\n"
"}")
        self.gridLayout_13 = QGridLayout(self.photo_page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(70)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.previous_pushButton = QPushButton(self.photo_page)
        self.previous_pushButton.setObjectName(u"previous_pushButton")
        sizePolicy4.setHeightForWidth(self.previous_pushButton.sizePolicy().hasHeightForWidth())
        self.previous_pushButton.setSizePolicy(sizePolicy4)
        icon5 = QIcon()
        icon5.addFile(u":/no_active/no_active/arrow_back_ios.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_pushButton.setIcon(icon5)
        self.previous_pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_7.addWidget(self.previous_pushButton)

        self.next_pushButton = QPushButton(self.photo_page)
        self.next_pushButton.setObjectName(u"next_pushButton")
        sizePolicy4.setHeightForWidth(self.next_pushButton.sizePolicy().hasHeightForWidth())
        self.next_pushButton.setSizePolicy(sizePolicy4)
        icon6 = QIcon()
        icon6.addFile(u":/no_active/no_active/arrow_forward_ios.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_pushButton.setIcon(icon6)
        self.next_pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_7.addWidget(self.next_pushButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.gridLayout_13.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.label_2 = QLabel(self.photo_page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_13.addWidget(self.label_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.photo_page)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.ProdgectBar = QWidget(self.centralwidget)
        self.ProdgectBar.setObjectName(u"ProdgectBar")
        sizePolicy7.setHeightForWidth(self.ProdgectBar.sizePolicy().hasHeightForWidth())
        self.ProdgectBar.setSizePolicy(sizePolicy7)
        self.ProdgectBar.setMinimumSize(QSize(0, 25))
        self.ProdgectBar.setMaximumSize(QSize(16777215, 25))
        self.ProdgectBar.setStyleSheet(u"#ProdgectBar {\n"
"background-color: rgba(246, 247, 240, 73);\n"
"}\n"
"QPushButton {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"height: 29px;\n"
"font-size: 16pt;\n"
"}\n"
"")
        self.gridLayout_7 = QGridLayout(self.ProdgectBar)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, -1, 6)
        self.save_prodgect_pushButton = QPushButton(self.ProdgectBar)
        self.save_prodgect_pushButton.setObjectName(u"save_prodgect_pushButton")
        sizePolicy4.setHeightForWidth(self.save_prodgect_pushButton.sizePolicy().hasHeightForWidth())
        self.save_prodgect_pushButton.setSizePolicy(sizePolicy4)
        self.save_prodgect_pushButton.setMinimumSize(QSize(95, 16))

        self.horizontalLayout.addWidget(self.save_prodgect_pushButton)

        self.prodgect_pushButton = QPushButton(self.ProdgectBar)
        self.prodgect_pushButton.setObjectName(u"prodgect_pushButton")
        sizePolicy4.setHeightForWidth(self.prodgect_pushButton.sizePolicy().hasHeightForWidth())
        self.prodgect_pushButton.setSizePolicy(sizePolicy4)
        self.prodgect_pushButton.setMinimumSize(QSize(95, 16))
        self.prodgect_pushButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.prodgect_pushButton)


        self.gridLayout_7.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(1549, 9, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.ProdgectBar, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.new_pushButton.clicked["bool"].connect(self.ProdgectBar.setVisible)
        self.new_pushButton.clicked["bool"].connect(self.ModelBar.setVisible)
        self.new_pushButton.clicked["bool"].connect(self.NeuralBar.setVisible)
        self.new_pushButton.clicked["bool"].connect(self.AnntBar.setVisible)
        self.new_pushButton.clicked["bool"].connect(self.ClassesBar.setVisible)
        self.new_pushButton.clicked["bool"].connect(self.DirectoryBar.setVisible)
        self.prodgect_pushButton.clicked["bool"].connect(self.ClassesBar.setHidden)
        self.prodgect_pushButton.clicked["bool"].connect(self.AnntBar.setHidden)
        self.prodgect_pushButton.clicked["bool"].connect(self.NeuralBar.setHidden)
        self.prodgect_pushButton.clicked["bool"].connect(self.ModelBar.setHidden)
        self.prodgect_pushButton.clicked["bool"].connect(self.DirectoryBar.setHidden)
        self.prodgect_pushButton.clicked["bool"].connect(self.ProdgectBar.setHidden)
        self.new_pushButton.clicked["bool"].connect(self.VideoSroll.setVisible)
        self.prodgect_pushButton.clicked["bool"].connect(self.VideoSroll.setHidden)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.class_label.setText(QCoreApplication.translate("MainWindow", u"Classes", None))
        self.create_pushButton.setText(QCoreApplication.translate("MainWindow", u"Create class", None))
        self.rename_pushButton.setText(QCoreApplication.translate("MainWindow", u"Rename class", None))
        self.delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete class", None))
        self.annotation_label.setText(QCoreApplication.translate("MainWindow", u"Annotation", None))
        self.create_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Create annt", None))
        self.delete_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete all annt", None))
        self.delete_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Delete annt", None))
        self.neural_label.setText(QCoreApplication.translate("MainWindow", u"Neural annt", None))
        self.auto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Auto annt", None))
        self.delete_pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Delete annt", None))
        self.save_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save annt", None))
        self.model_icon_label.setText("")
        self.model_label.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.track_pushButton.setText(QCoreApplication.translate("MainWindow", u"Track", None))
        self.save_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save video", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"autoannt", None))
        self.choose_pushButton.setText(QCoreApplication.translate("MainWindow", u"choose directory", None))
        self.new_pushButton.setText(QCoreApplication.translate("MainWindow", u"new project", None))
        self.label_3.setText("")
        self.previous_frame_pushButton.setText("")
        self.next_frame_pushButton.setText("")
        self.play_pushButton.setText("")
        self.screen_pushButton.setText("")
        self.neural_pushButton.setText("")
        self.previous_pushButton.setText("")
        self.next_pushButton.setText("")
        self.label_2.setText("")
        self.save_prodgect_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.prodgect_pushButton.setText(QCoreApplication.translate("MainWindow", u"Project", None))
    # retranslateUi

