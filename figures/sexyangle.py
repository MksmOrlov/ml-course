import logging

from figures.figure import PlanarFigure
from figures.triangle import Triangle

logger = logging.getLogger(__name__)

class SexyAngle(PlanarFigure):
    params_number = 1
    params_name = "Сторона"

    def __init__(self, side):
        super().__init__()
        self._side = side

    def _calculate_area(self) -> float:
        """Площадь этой смешной фигуры равна площади большого треугольника со стороной 3a
            и двум плозадям маленьких треугольников со стороной a"""
        big_triangle_side = self._side * 3
        big_triangle = Triangle(big_triangle_side, big_triangle_side, big_triangle_side)
        small_triangle = Triangle(self._side, self._side, self._side)

        area = big_triangle.get_area() + small_triangle.get_area() * 2
        self._area = area
        return area

    def _calculate_perimeter(self) -> float:
        perimeter = self._side * 16
        self._perimeter = perimeter
        return perimeter

    def print_answer(self):
        area = self._calculate_area()
        logger.info(f"S, приведённое к целочисленному типу: {int(area)}")
