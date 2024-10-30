"""
Main.
"""

from abc import ABC, abstractmethod
from numbers import Number


class Observer(ABC):
    """
    Observer abstract base class.
    """

    def __init__(self, name: str) -> None:
        """
        Constructor.
        :param name: Name of the observer
        """
        self.name = name

    @abstractmethod
    def Update(self, message: str) -> None:
        """
        Abstract Update method interface.

        :param message: Message received.
        :return:
        """
        print("Somehow in base class observer update method")


class Subject(ABC):
    """
    Subject abstract base class.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self._observers = []

    def AddObserver(self, observer: Observer) -> None:
        """
        Adds an observer.

        :param observer: Observer to add.
        """
        self._observers.append(observer)

    def RemoveObserver(self, observer) -> None:
        """
        Removes an observer.

        :param observer: Observer to remove.
        """
        self._observers.remove(observer)

    def UpdateObservers(self, message) -> None:
        """
        Updates observers.

        :param message: Message to send to observers.
        """
        for observer in self._observers:
            observer.Update(message)


class TemperatureSensor(Subject):
    """
    Temperature sensor subject.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self) -> Number:
        """
        Temperature property getter.
        :return: Temperature.
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: Number):
        """
        Temperature property setter.

        :param temperature: Temperature to set.
        :return:
        """
        self._temperature = temperature
        self.UpdateObservers(message=f"Temperature updated to {temperature}")


class MobileDisplay(Observer):
    """
    Mobile display observer.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__("mobile_display")

    def Update(self, message: str) -> None:
        """
        Updates mobile display.

        :param message: Message received.
        """
        print(f"Mobile display received message {message}")


class BackendMonitor(Observer):
    """
    Backend monitor observer.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__("backend_monitor")

    def Update(self, message: str) -> None:
        """
        Backend monitor observer.
        :param message: Message received.
        """
        print(f"Backend monitor received message {message}")


if __name__ == "__main__":

    mobileDisplay = MobileDisplay()
    backendMonitor = BackendMonitor()

    temperatureSensor = TemperatureSensor()
    temperatureSensor.AddObserver(mobileDisplay)
    temperatureSensor.AddObserver(backendMonitor)

    temperatureSensor.temperature = 10
    temperatureSensor.temperature = 20
