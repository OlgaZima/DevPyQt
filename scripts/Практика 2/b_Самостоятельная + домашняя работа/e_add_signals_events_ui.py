"""
Подключение формы созданной в дизайнере

Команда для конвертации формы:
PySide6-uic path_to_form.ui -o path_to_form.py
"""
import datetime

from PySide6 import QtWidgets, QtGui

from ui.c_signals_events import Ui_Form  # Импортируем класс формы


class Form(QtWidgets.QWidget):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.ui.initSignals()
        self.initSignals()


    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
       Cобытие изменения положения окна
       :param event: QtGui.QMoveEvent
       return: None
       """
        print(event.oldPos(), (datetime.datetime.today()).strftime('%H:%M'))
        print(event.pos(), (datetime.datetime.today()).strftime('%H:%M'))
        print()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """
        print(event.size(), (datetime.datetime.today()).strftime('%H:%M'))
        print()


    def initSignals(self):
        self.ui.pushButtonLT.clicked.connect(self.onClickLT)
        self.ui.pushButtonRT.clicked.connect(self.onClickRT)
        self.ui.pushButtonLB.clicked.connect(self.onClickLB)
        self.ui.pushButtonRB.clicked.connect(self.onClickRB)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onMove)
        self.ui.pushButtonCenter.clicked.connect(self.onClickC)
        self.ui.pushButtonGetData.clicked.connect(self.onClickGD)

    def onClickLT(self):
        self.move(0, 0)

    def onClickRT(self):
        self.move(700, 0)

    def onClickLB(self):
        self.move(0, 210)
        print("njnj")

    def onClickRB(self):
        self.move(700, 210)

    def onClickC(self):
        self.move(350, 105)

    def onMove(self):
        x = self.ui.spinBoxX.value()
        y = self.ui.spinBoxY.value()
        self.move(x, y)
        self.ui.plainTextEdit.setPlainText(str(self.pos()))
        self.ui.plainTextEdit.setPlainText(str(self.size()))

    def onClickGD(self):

        if self.isActiveWindow():
            status = "активно"
        else:
            status = "не активно"
        if self.isMaximized():
            status = "развёрнуто"

        if self.isMinimized():
            status = "свернуто"

        text = "время выполнения = " + str((datetime.datetime.today()).strftime('%H:%M')) + '\n'
        #text += "положение = " + str(self.pos()) + '\n'
        text += "положение X = " + str(self.x()) + '\n'
        text += "положение Y = " + str(self.y()) + '\n'
        #text += "размер = " + str(self.size()) + '\n'
        text += "ширина = " + str(self.width()) + '\n'
        text += "высота = " + str(self.height()) + '\n'
        text += "минимальный размер экрана =" + str(self.minimumSize()) + '\n'
        text += "состояние =" + status + '\n'

        self.ui.plainTextEdit.setPlainText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Form()
    window.show()

    app.exec()

