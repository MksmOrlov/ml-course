import logging
from figures.figure import PlanarFigure

logger = logging.getLogger(__name__)


class Rhombus(PlanarFigure):
    params_number = 2
    params_name = "Диагональ"

    def __init__(self, diagonal_1: float, diagonal_2: float):
        super().__init__()
        self._diagonal_1 = diagonal_1
        self._diagonal_2 = diagonal_2
        self._side = None

    def _calculate_perimeter(self) -> float:
        if self._perimeter:
            return self._perimeter
        a = self._diagonal_1 / 2
        b = self._diagonal_2 / 2
        side = (a * a + b * b) ** 0.5
        perimeter = side * 4

        self._side = side
        self._perimeter = perimeter
        return perimeter

    def _calculate_area(self) -> float:
        area = self._diagonal_1 * self._diagonal_2 / 2
        self._area = area
        return area

    def print_answer(self):
        area = self.get_area()
        logger.info(f"S, приведённое к целочисленному типу: {int(area)}")
        logger.info(f"S, округлённое до 1 знака после запятой с помощью функции  round(): {round(area)}")
        logger.info(f"S, точное значение без округления: {area}")
