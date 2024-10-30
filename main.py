"""
Main.
"""
from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def Update(self, message: str):
        print("Somehow in base class observer update method")

class Subject(ABC):

    def __init__(self):
        self._observers = []

    def AddObserver(self, observer: Observer):
        self._observers.append(observer)

    def RemoveObserver(self, observer):
        self._observers.remove(observer)

    def UpdateObservers(self, message):
        for observer in self._observers:
            observer.Update(message)

class TemperatureSensor(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature
        self.UpdateObservers(message=f"Temperature updated to {temperature}")

class MobileDisplay(Observer):
    def __init__(self):
        super().__init__("mobile_display")

    def Update(self, message: str):
        print(f"Mobile dispaly received message {message}")

class BackendMonitor(Observer):
    def __init__(self):
        super().__init__("backend_monitor")

    def Update(self, message: str):
        print(f"Backend monitor received message {message}")


if __name__ == "__main__":



    mobileDisplay = MobileDisplay()
    backendMonitor = BackendMonitor()

    temperatureSensor = TemperatureSensor()
    temperatureSensor.AddObserver(mobileDisplay)
    temperatureSensor.AddObserver(backendMonitor)

    temperatureSensor.temperature = 10
    temperatureSensor.temperature = 20

