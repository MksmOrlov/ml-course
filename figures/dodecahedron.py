import logging

from figures.figure import Figure

logger = logging.getLogger(__name__)


class Dodecahedron(Figure):
    params_number = 1
    params_name = "Сторона"

    def __init__(self, side):
        self._area = None
        self._side = side

    def _calculate_area(self) -> float:
        area = self._side * self._side * 3 * (5 * (5 + 2 * 5 ** 0.5)) ** 0.5
        self._area = area
        return area

    def get_area(self) -> float:
        if self._area:
            return self._area
        area = self._calculate_area()
        return area

    def print_answer(self):
        area = self._calculate_area()
        logger.info(f"S, округлённое до 2 знаков после запятой с помощью функции round(): {round(area, 2)}")
