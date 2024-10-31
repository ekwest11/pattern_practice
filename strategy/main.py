"""
Main.
"""
import inspect
from typing import Callable, Dict, List, Optional


def SortInterface(data: List[Dict]) -> List[Dict]:
    """
    Sorting interface.

    :param data: Data to sort.
    :return: A sorted copy of the input list.
    """
    pass


def SortByName(data: List[Dict]) -> List[Dict]:
    """
    Sorts data by name.

    :param data: Data to sort.
    :return: Data copy, sorted by name.
    """
    return sorted(data, key=lambda x: x["name"])


def SortByPrice(data: List[Dict]) -> List[Dict]:
    """
    Sorts data by price.

    :param data: Data to sort.
    :return: Data copy, sorted by price.
    """
    return sorted(data, key=lambda x: x["price"])


def SortByRating(data: List[Dict]) -> List[Dict]:
    """
    Sorts data by rating.

    :param data: Data to sort.
    :return: Data copy, sorted by rating.
    """
    return sorted(data, key=lambda x: x["rating"])


class Sorter:
    """
    Sorter class.
    """

    def __init__(self, initialStrategy: Optional[Callable] = None):
        """
        Constructor.

        :param initialStrategy: Initial strategy.
        """

        # Initialize the strategy.
        self.strategy = SortByName if not initialStrategy else initialStrategy
        self.strategyInterface = inspect.signature(SortInterface)

    def Sort(self, data: List[Dict]) -> List[Dict]:
        """
        Sorts the data.

        :param data: Data to sort.
        :return: Sorted data in a new list copy.
        """
        return self.strategy(data)

    def SetStrategy(self, strategy: Callable) -> None:
        """
        Set the sorting strategy.

        :param strategy:
        :return:
        """

        # Enforce the strategy prototype signature.
        if inspect.signature(strategy) != self.strategyInterface:
            raise Exception

        # Set the strategy.
        self.strategy = strategy


def FormatData(dataToFormat: List[Dict]) -> str:
    """
    Formats data to print.

    :param dataToFormat: Data to format.
    :return: Formatted string data to print.
    """

    # Get field widths.
    nameWidth = max(len(item["name"]) for item in dataToFormat)
    priceWidth = max(len(f"{item['price']}") for item in dataToFormat)
    ratingWidth = 6

    # Print header
    header = f"{'Name' :<{nameWidth}} | {'Price' :>{priceWidth}} |  {'Ratings' :>{ratingWidth}}\n"
    data = ""

    # Data rows
    for item in dataToFormat:
        data += f"{item['name']:<{nameWidth}} | {item['price']:>{priceWidth}} | {item['rating']:>{ratingWidth}.1f}\n"

    # Return formatted data.
    return header + data


if __name__ == "__main__":
    dataCatalog = [
        {"name": "Laptop", "price": 1200, "rating": 4.7},
        {"name": "Smartphone", "price": 800, "rating": 4.5},
        {"name": "Tablet", "price": 300, "rating": 4.2},
        {"name": "Smartwatch", "price": 200, "rating": 4.1},
    ]

    sorter = Sorter(initialStrategy=SortByName)
    print(f"Sorted by name is \n{FormatData(sorter.Sort(dataCatalog))}")

    sorter.SetStrategy(strategy=SortByPrice)
    print(f"Sorted by price is \n{FormatData(sorter.Sort(dataCatalog))}")

    sorter.SetStrategy(strategy=SortByRating)
    print(f"Sorted by rating is \n{FormatData(sorter.Sort(dataCatalog))}")
