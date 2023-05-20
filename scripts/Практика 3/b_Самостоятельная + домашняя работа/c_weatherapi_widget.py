"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для

2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
import time
from a_threads import WeatherHandler


from PySide6 import QtCore, QtWidgets

class WindowWeather(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #self.initThreads()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.label_weather = QtWidgets.QLabel("Weather: ")
        self.pushButton_start = QtWidgets.QPushButton("Запустить поток")
        self.pushButton_stop = QtWidgets.QPushButton("Остановить поток")
        self.spinbox_lat = QtWidgets.QDoubleSpinBox()
        self.spinbox_lon = QtWidgets.QDoubleSpinBox()
        self.spinbox_lat.setRange(-90.0, 90.0)
        self.spinbox_lon.setRange(-180.0, 180.0)
        self.spinbox_lat.setValue(73.5)
        self.spinbox_lon.setValue(83.3)
        self.spinbox_time = QtWidgets.QSpinBox()
        self.label_lat = QtWidgets.QLabel("Широта")
        self.label_lon = QtWidgets.QLabel("Долгота")
        self.label_time = QtWidgets.QLabel("Время задержки")
        self.plainTextEditWeather = QtWidgets.QPlainTextEdit()

        layout_weather = QtWidgets.QVBoxLayout()
        layout_weather.addWidget(self.label_weather)
        layout_weather.addWidget(self.plainTextEditWeather)
        layout_weather.addWidget(self.pushButton_start)
        layout_weather.addWidget(self.pushButton_stop)

        layout_lat = QtWidgets.QVBoxLayout()
        layout_lat.addWidget(self.label_lat)
        layout_lat.addWidget(self.spinbox_lat)

        layout_lon = QtWidgets.QVBoxLayout()
        layout_lon.addWidget(self.label_lon)
        layout_lon.addWidget(self.spinbox_lon)

        layout_time = QtWidgets.QVBoxLayout()
        layout_time.addWidget(self.label_time)
        layout_time.addWidget(self.spinbox_time)

        layot = QtWidgets.QHBoxLayout()
        layot.addLayout(layout_lat)
        layot.addLayout(layout_lon)
        layot.addLayout(layout_time)
        layot.addLayout(layout_weather)

        self.setLayout(layot)

    # def initThreads(self) -> None:
    #     self.weather_thread = WeatherHandler()

    def initSignals(self) -> None:
        self.pushButton_start.clicked.connect(self.onStart)
        self.pushButton_stop.clicked.connect(self.onStop)


    def onStart(self):
        self.weather_thread = WeatherHandler(self.spinbox_lat.value(), self.spinbox_lon.value())
        self.weather_thread.setDelay(self.spinbox_time.value())
        self.weather_thread.data_response.connect(self.ip_updated)

        self.spinbox_lat.setReadOnly(True)
        self.spinbox_lon.setEnabled(False)
        self.spinbox_time.setEnabled(False)

        self.weather_thread.started.connect(lambda: print("Поток погоды запущен"))
        #self.weather_thread.setStatus(True)
        self.weather_thread.start()


    def onStop(self):
        self.weather_thread.stop()
        self.weather_thread.finished.connect(lambda: print("Поток погоды остановлен"))
        #self.weather_thread.setStatus(False)
        self.spinbox_lat.setReadOnly(False)
        self.spinbox_lon.setEnabled(True)
        self.spinbox_time.setEnabled(True)


    def ip_updated(self, data: dict):
        self.plainTextEditWeather.appendPlainText(f"Обновлено: {time.ctime()}\n{str(data)}")
        print(f"{time.ctime()} поток погоды запущен")

    # def setTime(self, delay):
    #     self.weather_thread.setDelay(delay)

    # def set_Lat(self, lat_):
    #     self.weather_thread.setLat(lat_)
    #
    # def set_Lon(self, lon_):
    #     self.weather_thread.setLon(lon_)

    # def initSignals(self) -> None:
    #
    #     self.pushButton_start.clicked.connect(self.start_)
    #     self.spinbox_time.valueChanged.connect(self.setTime)
    #     #self.weather_thread.finished.connect(lambda: print("Поток остановлен"))
    #     self.weather_thread.data_responsed.connect(self.ip_updated)
    #     # self.spinbox_lat.valueChanged.connect(self.set_Lat)
    #     # self.spinbox_lon.valueChanged.connect(self.set_Lon)



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()