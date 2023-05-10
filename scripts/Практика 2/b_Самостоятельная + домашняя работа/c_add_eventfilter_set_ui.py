"""
Подключение формы созданной в дизайнере

Команда для конвертации формы:
PySide6-uic path_to_form.ui -o path_to_form.py
"""
import datetime

from PySide6 import QtWidgets, QtGui, QtCore

from ui.eventfilter_set import Ui_Form  # Импортируем класс формы


class Form(QtWidgets.QWidget):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = QtCore.QSettings("MyDataCard")
        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()
        self.loadData()

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_Plus:
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        elif event.key() == QtCore.Qt.Key_Minus:
            self.ui.dial.setValue(self.ui.dial.value() - 1)

    def initSignals(self):
        self.ui.dial.valueChanged.connect(self.onDial)
        self.ui.horizontalSlider.valueChanged.connect(self.onSlider)
        self.ui.comboBox.currentTextChanged.connect(self.onLcdNumber)

    def onDial(self):
        self.ui.lcdNumber.display(self.ui.dial.value())
        print(int(self.ui.lcdNumber.value()))
        self.ui.horizontalSlider.setValue(self.ui.dial.value())

    def onSlider(self):
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())
        self.ui.dial.setValue(self.ui.horizontalSlider.value())

    def onLcdNumber(self):
        if self.ui.comboBox.currentText() == "oct":
            self.ui.lcdNumber.setOctMode()
        if self.ui.comboBox.currentText() == "hex":
            self.ui.lcdNumber.setHexMode()
        if self.ui.comboBox.currentText() == "bin":
            self.ui.lcdNumber.setBinMode()
        if self.ui.comboBox.currentText() == "dec":
            self.ui.lcdNumber.setDecMode()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings.setValue("Text", self.ui.comboBox.currentText())
        self.settings.setValue("Text2", self.ui.lcdNumber.value())

    def loadData(self):
        self.ui.comboBox.setCurrentText(self.settings.value("Text", ""))
        self.ui.lcdNumber.display(self.settings.value("Text2", 1))
        self.ui.dial.setValue(self.ui.lcdNumber.value())
        self.ui.horizontalSlider.setValue(self.ui.lcdNumber.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Form()
    window.show()

    app.exec()

