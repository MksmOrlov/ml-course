import logging

from figures.figure import PlanarFigure
from figures.triangle import Triangle

logger = logging.getLogger(__name__)


class HexagonFriends(PlanarFigure):
    params_number = 1
    params_name = "Сторона"

    def __init__(self, side):
        super().__init__()
        self._side = side

    def _calculate_area(self):
        hexagon_area = 3 * (3 ** 0.5) * 0.5 * self._side * self._side
        square_area = self._side * self._side

        triangle_side = self._side / 2
        triangle = Triangle(triangle_side, triangle_side, triangle_side)
        triangle_area = triangle.get_area()
        area = hexagon_area + square_area * 3 + triangle_area * 6
        self._area = area
        return area

    def _calculate_perimeter(self):
        pass

    def print_answer(self) -> None:
        area = self.get_area()
        logger.info(f"S, приведённое к целочисленному типу: {int(area)}")
