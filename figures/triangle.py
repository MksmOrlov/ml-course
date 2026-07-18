import logging

from figures.figure import PlanarFigure

logger = logging.getLogger(__name__)

class Triangle(PlanarFigure):
    params_number = 3
    params_name = "Сторона"

    def __init__(self, side_1: float, side_2: float, side_3: float):
        super().__init__()
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def get_sides(self) -> tuple[float, float, float]:
        return self._side_1, self._side_2, self._side_3

    @staticmethod
    def verify(params: list) -> bool:
        """Проверка на вырожденность с помощью неравенства треугольника"""
        if (params[0] < params[1] + params[2] and
                params[1] < params[0] + params[2] and
                params[2] < params[0] + params[1]):
            return True
        logger.warning(f"Треугольник со сторонами {params[0], params[1], params[2]} вырожден")
        return False

    def _calculate_perimeter(self) -> float:
        perimeter = self._side_1 + self._side_2 + self._side_3
        perimeter = round(perimeter, 3)
        self._perimeter = perimeter
        return perimeter

    def _calculate_area(self) -> float:
        """Формула Герона"""
        if self._perimeter is None:
            self._calculate_perimeter()
        perimeters_expression = (self._side_1 + self._side_2 + self._side_3) * (self._side_2 + self._side_3 - self._side_1) * (self._side_1 + self._side_3 - self._side_2) * (self._side_1 + self._side_2 - self._side_3)
        square = 0.25 * (perimeters_expression ** 0.5)
        square = round(square, 3)
        self._square = square
        return square

    def print_answer(self):
        perimeter = self.get_perimeter()
        area = self.get_area()

        logger.info(f"Периметр треугольника: {perimeter}")
        logger.info(f"Площадь треугольника: {area}")
