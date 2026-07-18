import logging

from figures.figure import Figure

logger = logging.getLogger(__name__)

class Triangle(Figure):
    def __init__(self, side_1: float, side_2: float, side_3: float):
        super().__init__()
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def get_sides(self) -> tuple[float, float, float]:
        return self._side_1, self._side_2, self._side_3

    @staticmethod
    def is_degenerate(side_1: float, side_2: float, side_3: float):
        """Проверка на вырожденность с помощью неравенства треугольника"""
        if (side_1 < side_2 + side_3 and
                side_2 < side_1 + side_3 and
                side_3 < side_1 + side_2):
            return False
        return True

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
        square = 0.25 * perimeters_expression ** 0.5
        square = round(square, 3)
        self._square = square
        return square

    def print_answer(self):
        perimeter = self.get_perimeter()
        area = self.get_area()

        logging.info(f"Периметр треуголька: {perimeter}")
        logging.info(f"Площадь треуголька: {area}")

class TriangleCreator:
    @staticmethod
    def create_triangle() -> Triangle:
        side_1, side_2, side_3 = TriangleCreator.get_triangle_sides()
        triangle = Triangle(side_1, side_2, side_3)
        return triangle

    @staticmethod
    def get_triangle_sides() -> tuple[float, float, float]:
        side_1 = float(input("Введите 3 стороны треугольника\nПервая сторона: "))
        if not Figure.is_positive(side_1):
            side_1, side_2, side_3 = TriangleCreator.get_triangle_sides()
            logger.warning("Сторона должна принимать положительное значение")
        side_2 = float(input("Вторая сторона: "))
        if not Figure.is_positive(side_2):
            side_1, side_2, side_3 = TriangleCreator.get_triangle_sides()
            logger.warning("Сторона должна принимать положительное значение")
        side_3 = float(input("Третья сторона: "))
        if not Figure.is_positive(side_3):
            side_1, side_2, side_3 = TriangleCreator.get_triangle_sides()
            logger.warning("Сторона должна принимать положительное значение")

        if Triangle.is_degenerate(side_1, side_2, side_3):
            logging.warning(f"Треугольник со сторонами {side_1, side_2, side_3} вырожден")
            side_1, side_2, side_3 = TriangleCreator.get_triangle_sides()

        return side_1, side_2, side_3

def calculate_triangle():
    try:
        triangle = TriangleCreator.create_triangle()

        logging.debug(f"Создан треугольник со сторонами: {triangle.get_sides()}")
        triangle.print_answer()
    except KeyboardInterrupt:
        logging.warning("Ввод прерван пользователем")
    except ValueError:
        logging.warning("Введите число")
        calculate_triangle()
