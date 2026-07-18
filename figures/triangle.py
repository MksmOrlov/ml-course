import logging

logger = logging.getLogger(__name__)

class Triangle:
    def __init__(self, side_1: float, side_2: float, side_3: float):
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

        self._perimeter = None
        self._square = None

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

    def calculate_triangle_perimeter(self) -> float:
        if self._perimeter:
            return self._perimeter

        perimeter = self._side_1 + self._side_2 + self._side_3
        perimeter = round(perimeter, 3)
        self._perimeter = perimeter
        return perimeter

    def calculate_triangle_square(self) -> float:
        """Формула Герона"""
        if self._square:
            return self._square

        if self._perimeter is None:
            self.calculate_triangle_perimeter()
        perimeters_expression = (self._side_1 + self._side_2 + self._side_3) * (self._side_2 + self._side_3 - self._side_1) * (self._side_1 + self._side_3 - self._side_2) * (self._side_1 + self._side_2 - self._side_3)
        square = 0.25 * perimeters_expression ** 0.5
        square = round(square, 3)
        self._square = square
        return square

class TriangleCreator:
    @staticmethod
    def create_triangle() -> Triangle:
        side_1, side_2, side_3 = TriangleCreator.get_triangle_sides()
        triangle = Triangle(side_1, side_2, side_3)
        return triangle

    @staticmethod
    def get_triangle_sides() -> tuple[float, float, float]:
        side_1 = float(input("Введите 3 стороны треугольника (каждая с новой строки)\nПервая сторона: "))
        side_2 = float(input("Вторая сторона: "))
        side_3 = float(input("Третья сторона: "))

        if Triangle.is_degenerate(side_1, side_2, side_3):
            logging.warning(f"Треугольник со сторонами {side_1, side_2, side_3} вырожден")
            side_1, side_2, side_3 = TriangleCreator.get_triangle_sides()

        return side_1, side_2, side_3

def calculate_triangle():
    try:
        triangle = TriangleCreator.create_triangle()
        perimeter = triangle.calculate_triangle_perimeter()
        square = triangle.calculate_triangle_square()

        logging.debug(f"Создан треугольник со сторонами: {triangle.get_sides()}")
        logging.info(f"Периметр треуголька: {perimeter}")
        logging.info(f"Площадь треуголька: {square}")
    except KeyboardInterrupt:
        logging.warning("Ввод прерван пользователем")
    except ValueError:
        logging.warning("Введите число")
        calculate_triangle()
