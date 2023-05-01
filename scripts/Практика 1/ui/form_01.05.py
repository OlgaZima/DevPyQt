# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_01.05.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1078, 793)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1058, 730))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_2.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_2.addWidget(self.radioButton_2)


        self.horizontalLayout_5.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_3.addWidget(self.checkBox_3)


        self.horizontalLayout_6.addWidget(self.groupBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_3.addWidget(self.frame)

        self.toolBox_2 = QToolBox(self.tab)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 504, 476))
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit = QLineEdit(self.page_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_9.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_9.addWidget(self.lineEdit_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_10.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.page_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_10.addWidget(self.lineEdit_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 241, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.toolBox_2.addItem(self.page_3, u"QlineEdit")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 504, 476))
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textEdit = QTextEdit(self.page_4)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_9.addWidget(self.textEdit)

        self.toolBox_2.addItem(self.page_4, u"QTextEdit")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 504, 476))
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.plainTextEdit = QPlainTextEdit(self.page)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_8.addWidget(self.plainTextEdit)

        self.toolBox_2.addItem(self.page, u"QPlainTextEdit")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 504, 476))
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.calendarWidget = QCalendarWidget(self.page_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_7.addWidget(self.calendarWidget)

        self.toolBox_2.addItem(self.page_2, u"QCalendarWidget")

        self.horizontalLayout_3.addWidget(self.toolBox_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QSize(16777215, 181))
        font1 = QFont()
        font1.setPointSize(10)
        self.groupBox_7.setFont(font1)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(160, 0))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setKerning(True)
        self.label_9.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label_9)

        self.lineEdit_9 = QLineEdit(self.groupBox_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_20.addWidget(self.lineEdit_9)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(160, 0))
        self.label_10.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_22.addWidget(self.label_10)

        self.lineEdit_10 = QLineEdit(self.groupBox_7)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_22.addWidget(self.lineEdit_10)


        self.verticalLayout_21.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_11 = QLabel(self.groupBox_7)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(160, 0))
        self.label_11.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_23.addWidget(self.label_11)

        self.lineEdit_11 = QLineEdit(self.groupBox_7)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_23.addWidget(self.lineEdit_11)


        self.verticalLayout_21.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(160, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_24.addWidget(self.label_12)

        self.lineEdit_12 = QLineEdit(self.groupBox_7)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_24.addWidget(self.lineEdit_12)


        self.verticalLayout_21.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(160, 0))
        self.label_13.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_25.addWidget(self.label_13)

        self.lineEdit_13 = QLineEdit(self.groupBox_7)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_25.addWidget(self.lineEdit_13)


        self.verticalLayout_21.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_19.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMaximumSize(QSize(16777215, 181))
        self.groupBox_8.setFont(font1)
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_14 = QLabel(self.groupBox_8)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_26.addWidget(self.label_14)

        self.textEdit_6 = QTextEdit(self.groupBox_8)
        self.textEdit_6.setObjectName(u"textEdit_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy1)
        self.textEdit_6.setMinimumSize(QSize(85, 0))
        self.textEdit_6.setMaximumSize(QSize(90, 22))
        font3 = QFont()
        font3.setPointSize(11)
        self.textEdit_6.setFont(font3)
        self.textEdit_6.setFrameShape(QFrame.WinPanel)
        self.textEdit_6.setFrameShadow(QFrame.Sunken)
        self.textEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_26.addWidget(self.textEdit_6)


        self.verticalLayout_22.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_15 = QLabel(self.groupBox_8)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_27.addWidget(self.label_15)

        self.textEdit_7 = QTextEdit(self.groupBox_8)
        self.textEdit_7.setObjectName(u"textEdit_7")
        sizePolicy1.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy1)
        self.textEdit_7.setMinimumSize(QSize(85, 0))
        self.textEdit_7.setMaximumSize(QSize(90, 22))
        self.textEdit_7.setFont(font3)
        self.textEdit_7.setFrameShape(QFrame.WinPanel)
        self.textEdit_7.setFrameShadow(QFrame.Sunken)
        self.textEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_27.addWidget(self.textEdit_7)


        self.verticalLayout_22.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_16 = QLabel(self.groupBox_8)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_28.addWidget(self.label_16)

        self.textEdit_9 = QTextEdit(self.groupBox_8)
        self.textEdit_9.setObjectName(u"textEdit_9")
        sizePolicy1.setHeightForWidth(self.textEdit_9.sizePolicy().hasHeightForWidth())
        self.textEdit_9.setSizePolicy(sizePolicy1)
        self.textEdit_9.setMinimumSize(QSize(85, 0))
        self.textEdit_9.setMaximumSize(QSize(90, 22))
        self.textEdit_9.setFont(font3)
        self.textEdit_9.setFrameShape(QFrame.WinPanel)
        self.textEdit_9.setFrameShadow(QFrame.Sunken)
        self.textEdit_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_28.addWidget(self.textEdit_9)


        self.verticalLayout_22.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_17 = QLabel(self.groupBox_8)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_29.addWidget(self.label_17)

        self.textEdit_8 = QTextEdit(self.groupBox_8)
        self.textEdit_8.setObjectName(u"textEdit_8")
        sizePolicy1.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy1)
        self.textEdit_8.setMinimumSize(QSize(85, 0))
        self.textEdit_8.setMaximumSize(QSize(90, 22))
        self.textEdit_8.setFont(font3)
        self.textEdit_8.setFrameShape(QFrame.WinPanel)
        self.textEdit_8.setFrameShadow(QFrame.Sunken)
        self.textEdit_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_29.addWidget(self.textEdit_8)


        self.verticalLayout_22.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_18 = QLabel(self.groupBox_8)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_30.addWidget(self.label_18)

        self.textEdit_10 = QTextEdit(self.groupBox_8)
        self.textEdit_10.setObjectName(u"textEdit_10")
        sizePolicy1.setHeightForWidth(self.textEdit_10.sizePolicy().hasHeightForWidth())
        self.textEdit_10.setSizePolicy(sizePolicy1)
        self.textEdit_10.setMinimumSize(QSize(85, 0))
        self.textEdit_10.setMaximumSize(QSize(90, 22))
        self.textEdit_10.setFont(font3)
        self.textEdit_10.setFrameShape(QFrame.WinPanel)
        self.textEdit_10.setFrameShadow(QFrame.Sunken)
        self.textEdit_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_30.addWidget(self.textEdit_10)


        self.verticalLayout_22.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_19.addWidget(self.groupBox_8)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(16777215, 181))
        self.groupBox_6.setFont(font1)
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tableWidget = QTableWidget(self.groupBox_6)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(0, 255, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(brush1);
        __qtablewidgetitem8.setForeground(brush);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setBackground(brush1);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setBackground(brush1);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMaximumSize(QSize(16777215, 181))

        self.horizontalLayout_14.addWidget(self.tableWidget)


        self.horizontalLayout_19.addWidget(self.groupBox_6)


        self.verticalLayout_20.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.groupBox_10 = QGroupBox(self.groupBox_5)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMaximumSize(QSize(16777215, 185))
        self.groupBox_10.setFont(font1)
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_19 = QLabel(self.groupBox_10)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_31.addWidget(self.label_19)

        self.textEdit_2 = QTextEdit(self.groupBox_10)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 22))
        self.textEdit_2.setFrameShape(QFrame.WinPanel)
        self.textEdit_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_31.addWidget(self.textEdit_2)


        self.verticalLayout_23.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_22 = QLabel(self.groupBox_10)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_34.addWidget(self.label_22)

        self.textEdit_3 = QTextEdit(self.groupBox_10)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 22))
        self.textEdit_3.setFrameShape(QFrame.WinPanel)
        self.textEdit_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_34.addWidget(self.textEdit_3)


        self.verticalLayout_23.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_20 = QLabel(self.groupBox_10)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_32.addWidget(self.label_20)

        self.textEdit_4 = QTextEdit(self.groupBox_10)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(16777215, 22))
        self.textEdit_4.setFrameShape(QFrame.WinPanel)
        self.textEdit_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_32.addWidget(self.textEdit_4)


        self.verticalLayout_23.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_21 = QLabel(self.groupBox_10)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_33.addWidget(self.label_21)

        self.textEdit_5 = QTextEdit(self.groupBox_10)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(16777215, 22))
        self.textEdit_5.setFrameShape(QFrame.WinPanel)
        self.textEdit_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_33.addWidget(self.textEdit_5)


        self.verticalLayout_23.addLayout(self.horizontalLayout_33)


        self.verticalLayout_18.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.groupBox_5)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font1)
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSlider_8 = QSlider(self.groupBox_11)
        self.verticalSlider_8.setObjectName(u"verticalSlider_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.verticalSlider_8.sizePolicy().hasHeightForWidth())
        self.verticalSlider_8.setSizePolicy(sizePolicy3)
        self.verticalSlider_8.setOrientation(Qt.Vertical)

        self.verticalLayout_14.addWidget(self.verticalSlider_8)

        self.label_8 = QLabel(self.groupBox_11)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_14.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.horizontalLayout_13.addLayout(self.verticalLayout_14)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSlider_2 = QSlider(self.groupBox_11)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        sizePolicy3.setHeightForWidth(self.verticalSlider_2.sizePolicy().hasHeightForWidth())
        self.verticalSlider_2.setSizePolicy(sizePolicy3)
        self.verticalSlider_2.setMaximum(99)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.verticalLayout_11.addWidget(self.verticalSlider_2)

        self.label_2 = QLabel(self.groupBox_11)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2)


        self.horizontalLayout_13.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSlider_6 = QSlider(self.groupBox_11)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        sizePolicy3.setHeightForWidth(self.verticalSlider_6.sizePolicy().hasHeightForWidth())
        self.verticalSlider_6.setSizePolicy(sizePolicy3)
        self.verticalSlider_6.setOrientation(Qt.Vertical)

        self.verticalLayout_12.addWidget(self.verticalSlider_6)

        self.label_6 = QLabel(self.groupBox_11)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6)


        self.horizontalLayout_13.addLayout(self.verticalLayout_12)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSlider_26 = QSlider(self.groupBox_11)
        self.verticalSlider_26.setObjectName(u"verticalSlider_26")
        sizePolicy3.setHeightForWidth(self.verticalSlider_26.sizePolicy().hasHeightForWidth())
        self.verticalSlider_26.setSizePolicy(sizePolicy3)
        self.verticalSlider_26.setOrientation(Qt.Vertical)

        self.verticalLayout_15.addWidget(self.verticalSlider_26)

        self.label_26 = QLabel(self.groupBox_11)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_15.addWidget(self.label_26)


        self.horizontalLayout_13.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_3 = QSpacerItem(110, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSlider_7 = QSlider(self.groupBox_11)
        self.verticalSlider_7.setObjectName(u"verticalSlider_7")
        sizePolicy3.setHeightForWidth(self.verticalSlider_7.sizePolicy().hasHeightForWidth())
        self.verticalSlider_7.setSizePolicy(sizePolicy3)
        self.verticalSlider_7.setSliderPosition(0)
        self.verticalSlider_7.setOrientation(Qt.Vertical)

        self.verticalLayout_13.addWidget(self.verticalSlider_7)

        self.label_7 = QLabel(self.groupBox_11)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)


        self.horizontalLayout_13.addLayout(self.verticalLayout_13)


        self.verticalLayout_18.addWidget(self.groupBox_11)


        self.horizontalLayout_21.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_12 = QGroupBox(self.groupBox_5)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font1)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.progressBar_3 = QProgressBar(self.groupBox_12)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy3.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy3)
        self.progressBar_3.setValue(24)
        self.progressBar_3.setOrientation(Qt.Vertical)

        self.verticalLayout_16.addWidget(self.progressBar_3)

        self.label_23 = QLabel(self.groupBox_12)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMaximumSize(QSize(74, 18))
        self.label_23.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_23)


        self.horizontalLayout_15.addLayout(self.verticalLayout_16)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.progressBar_2 = QProgressBar(self.groupBox_12)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy3.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy3)
        self.progressBar_2.setMaximumSize(QSize(100, 16777215))
        self.progressBar_2.setValue(78)
        self.progressBar_2.setOrientation(Qt.Vertical)

        self.verticalLayout_24.addWidget(self.progressBar_2)

        self.label_27 = QLabel(self.groupBox_12)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(74, 18))

        self.verticalLayout_24.addWidget(self.label_27)


        self.horizontalLayout_15.addLayout(self.verticalLayout_24)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.progressBar_4 = QProgressBar(self.groupBox_12)
        self.progressBar_4.setObjectName(u"progressBar_4")
        sizePolicy3.setHeightForWidth(self.progressBar_4.sizePolicy().hasHeightForWidth())
        self.progressBar_4.setSizePolicy(sizePolicy3)
        self.progressBar_4.setMaximumSize(QSize(100, 16777215))
        self.progressBar_4.setMinimum(0)
        self.progressBar_4.setValue(100)
        self.progressBar_4.setOrientation(Qt.Vertical)

        self.verticalLayout_17.addWidget(self.progressBar_4)

        self.label_24 = QLabel(self.groupBox_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(74, 18))

        self.verticalLayout_17.addWidget(self.label_24)


        self.horizontalLayout_15.addLayout(self.verticalLayout_17)


        self.verticalLayout_19.addWidget(self.groupBox_12)

        self.groupBox_9 = QGroupBox(self.groupBox_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy1.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy1)
        self.groupBox_9.setMaximumSize(QSize(259, 261))
        self.groupBox_9.setFont(font1)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_5 = QPushButton(self.groupBox_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy4)
        self.pushButton_5.setMinimumSize(QSize(75, 75))
        self.pushButton_5.setMaximumSize(QSize(75, 75))
        font4 = QFont()
        font4.setPointSize(20)
        self.pushButton_5.setFont(font4)

        self.horizontalLayout_7.addWidget(self.pushButton_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_8 = QPushButton(self.groupBox_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy4.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy4)
        self.pushButton_8.setMinimumSize(QSize(75, 75))
        self.pushButton_8.setMaximumSize(QSize(75, 75))
        self.pushButton_8.setFont(font4)

        self.horizontalLayout_12.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.groupBox_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        self.pushButton_7.setMinimumSize(QSize(75, 75))
        self.pushButton_7.setMaximumSize(QSize(75, 75))
        self.pushButton_7.setFont(font4)

        self.horizontalLayout_12.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.groupBox_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)
        self.pushButton_6.setMinimumSize(QSize(75, 75))
        self.pushButton_6.setMaximumSize(QSize(75, 75))
        self.pushButton_6.setFont(font4)

        self.horizontalLayout_12.addWidget(self.pushButton_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)


        self.verticalLayout_19.addWidget(self.groupBox_9)


        self.horizontalLayout_21.addLayout(self.verticalLayout_19)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_18.addWidget(self.groupBox_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1078, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.action)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"QRadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"QCheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"QlineEdit", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"QTextEdit", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page), QCoreApplication.translate("MainWindow", u"QPlainTextEdit", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"QCalendarWidget", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u041a\u0410", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043e\u0440\u0431\u0438\u0442\u044b", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"10256 \u043a\u043c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"0,2 \u043c/\u0441", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u041a\u0410", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"364 \u043a\u043c/\u0447", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"60,00000", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"30,00000", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#efb328;\">22 \u00b0\u0421</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#50ff05;\">\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 1", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#50ff05;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 2", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 3", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u043e\u0432", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0435\u0441\u0441", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"36,6", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"140/70", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"36,8", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"120/60", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"36,5", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"130/70", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u044b\u0440 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 1", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 2", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 3", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#ffaa00;\">\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 4", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; color:#00ff00;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 3", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u2116 4", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043f\u043b\u0438\u0432\u043e", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 1", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 2", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u2116 3", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0430\u043d\u0435\u0432\u0440\u043e\u0432\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

