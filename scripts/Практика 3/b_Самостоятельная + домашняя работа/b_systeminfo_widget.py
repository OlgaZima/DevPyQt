#from a_threads import SystemInfo
from PySide6 import QtWidgets, QtCore

import time

import time
from PySide6 import QtCore
from a_threads import SystemInfo


class WindowSys(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #self.initThreads()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:

        self.labelTime = QtWidgets.QLabel("TIme:  ")
        self.labelCPU = QtWidgets.QLabel("CPU: ")
        self.labelRAM = QtWidgets.QLabel("RAM: ")
        self.barTime = QtWidgets.QSpinBox()
        self.barCPU = QtWidgets.QProgressBar()
        #self.barCPU.setRange(0, 100)
        self.barRAM = QtWidgets.QProgressBar()
        self.buttonStart = QtWidgets.QPushButton("Запусить задачу")
        self.buttonStop = QtWidgets.QPushButton("Остановить задачу")

        layout1 = QtWidgets.QVBoxLayout()
        layout1.addWidget(self.labelTime)
        layout1.addWidget(self.barTime)

        layout2 = QtWidgets.QVBoxLayout()
        layout2.addWidget(self.labelCPU)
        layout2.addWidget(self.barCPU)

        layout3 = QtWidgets.QVBoxLayout()
        layout3.addWidget(self.labelRAM)
        layout3.addWidget(self.barRAM)

        layout5 = QtWidgets.QHBoxLayout()
        layout5.addWidget(self.buttonStart)
        layout5.addWidget(self.buttonStop)

        layout4 = QtWidgets.QHBoxLayout()
        layout4.addLayout(layout1)
        layout4.addLayout(layout2)
        layout4.addLayout(layout3)

        layout6 = QtWidgets.QVBoxLayout()
        layout6.addLayout(layout4)
        layout6.addLayout(layout5)

        self.setLayout(layout6)

    def initSignals(self):
        self.buttonStart.clicked.connect(self.onStart)
        self.buttonStop.clicked.connect(self.onStop)

#
    def onStart(self):
        self.thread_SystemInfo = SystemInfo()
        self.thread_SystemInfo.systemInfoReceived.connect(self.updateData)
        self.thread_SystemInfo.setDelay(self.barTime.value())
        self.thread_SystemInfo.start()


    def updateData(self, CpuRam) -> None:
        self.barCPU.setValue(int(CpuRam[0]))
        self.barRAM.setValue(int(CpuRam[1][2]))
        print(time.ctime(), "CPU:", CpuRam[0], "%", ",", "RAM:", CpuRam[1][2], "%")

    def onStop(self):
        self.thread_SystemInfo.stop()
        self.thread_SystemInfo.finished.connect(lambda: print("Поток остановлен"))



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = WindowSys()
    window.show()

    app.exec()
#
#
# """
# Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads
#
# Создавать форму можно как в ручную, так и с помощью программы Designer
#
# Форма должна содержать:
# 1. поле для ввода времени задержки
# 2. поле для вывода информации о загрузке CPU
# 3. поле для вывода информации о загрузке RAM
# 4. поток необходимо запускать сразу при старте приложения
# 5. установку времени задержки сделать "горячей", т.е. поток должен сразу
# реагировать на изменение времени задержки
# """
