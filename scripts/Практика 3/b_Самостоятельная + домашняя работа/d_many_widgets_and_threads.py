"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
import psutil
from PySide6 import QtWidgets, QtGui, QtCore
from b_systeminfo_widget import WindowSys
from c_weatherapi_widget import WindowWeather

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) #здесь надо обязательго устанавливать parent
        self.centralwidget = QtWidgets.QWidget(self) #ссылаемся на свое главное окно, которое мы создали, centralwidget -это parent
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.app1 = WindowSys(self.centralwidget) #надо передать кто у него предок, он размещается на self.centralwidget
        self.app2 = WindowWeather(self.centralwidget) # у объектов лучше говорить кто у него родитель
        self.horizontalLayout.addWidget(self.app1) # размещаем в гор. layuot, а QMainWindow на centralwidget
        self.horizontalLayout.addWidget(self.app2)
        self.setCentralWidget(self.centralwidget) # QMainWinow use centralwidget, а не layout


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    main_window = MainWindow()
    main_window.show()

    app.exec()