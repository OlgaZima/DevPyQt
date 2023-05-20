"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil, requests
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)
    status_signal = QtCore.Signal(bool)

    def __init__(self, delay=None, parent=None):
        super().__init__(parent)
        self.delay = None  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def setDelay(self, delay):
        self.delay = delay

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:
            self.delay = 1  # TODO то устанавливайте значение 1
        self.status_signal.emit(True)
        while self.status_signal:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory()  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfoReceived.emit([cpu_value, ram_value])  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay
            CpuRam = [cpu_value, ram_value]
        self.stop()
    def stop(self):
        self.status_signal = False

class WeatherHandler(QtCore.QThread):
    # TODO Пропишите сигналы, которые считаете нужными
    data_response = QtCore.Signal(dict)
    status_signal = QtCore.Signal(bool)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)
        self.lat = lat
        self.lon = lon

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        # self.__status = None

    # def setLat(self, lat_):
    #     s = self.__api_url
    #     p = s.split('&', 2)
    #     s = s.replace(p[0], 'https://api.open-meteo.com/v1/forecast?latitude=' + str(int(lat_)))
    #     self.__api_url = s
    #
    # def setLon(self, lon_):
    #     s = self.__api_url
    #     p = s.split('&', 2)
    #     s = s.replace(p[1], 'longitude='+str(int(lon_)))
    #     self.__api_url = s

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    # def setStatus(self, status):
    #     """
    #     Метод для установки status signals: True or False
    #     """
    #     self.__status = status


    def run(self) -> None:
        # TODO настройте метод для корректной работы
        if self.__delay == 0:
            self.__delay = 10
        self.status_signal.emit(True)

        while self.status_signal:
            try:
                response = requests.get(self.__api_url)
                data = response.json()
                self.data_response.emit(data)
                time.sleep(self.__delay)

            except requests.exceptions.ConnectionError:
                print("Проверьте подклучение к сети, эта сессия завершена")
                self.stop()
        self.stop()

    def stop(self):
        self.status_signal = False

