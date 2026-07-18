import logging
from abc import ABC, abstractmethod

from user_input_processor import ObjectCalculator

logger = logging.getLogger(__name__)

class Figure(ABC, ObjectCalculator):
    @abstractmethod
    def print_answer(self) -> None:
        pass

    @staticmethod
    def verify(params: list) -> bool:
        return True


class PlanarFigure(Figure):
    def __init__(self):
        self._area: float | None = None
        self._perimeter: float | None = None

    @abstractmethod
    def _calculate_perimeter(self) -> float:
        pass

    @abstractmethod
    def _calculate_area(self) -> float:
        pass

    def get_area(self) -> float:
        if self._area is None:
            self._area = self._calculate_area()
        return self._area

    def get_perimeter(self) -> float:
        if self._perimeter is None:
            self._perimeter = self._calculate_perimeter()
        return self._perimeter
