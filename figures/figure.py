from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self):
        self._area: float | None = None
        self._perimeter: float | None = None

    @abstractmethod
    def _calculate_perimeter(self) -> float:
        pass

    @abstractmethod
    def _calculate_area(self) -> float:
        pass

    @staticmethod
    def is_positive(number: float) -> bool:
        return number > 0

    def get_area(self) -> float:
        if self._area is None:
            self._area = self._calculate_area()
        return self._area

    def get_perimeter(self) -> float:
        if self._perimeter is None:
            self._perimeter = self._calculate_perimeter()
        return self._perimeter
