import logging
from figures.figure import Figure

logger = logging.getLogger(__name__)


class Rhombus(Figure):
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

class RhombusCreator:
    @staticmethod
    def create_rhombus() -> Rhombus:
        diagonal_1, diagonal_2 = RhombusCreator.get_rhombus_diagonals()
        rhombus = Rhombus(diagonal_1, diagonal_2)
        return rhombus

    @staticmethod
    def get_rhombus_diagonals() -> tuple[float, float]:
        diagonal_1 = float(input("Введите 2 диагонали ромба\nПервая диагональ: "))
        if not Figure.is_positive(diagonal_1):
            diagonal_1, diagonal_2 = RhombusCreator.get_rhombus_diagonals()
            logger.warning("Диагональ должна принимать положительное значение")
        diagonal_2 = float(input("Вторая диагональ: "))
        if not Figure.is_positive(diagonal_2):
            diagonal_1, diagonal_2 = RhombusCreator.get_rhombus_diagonals()
            logger.warning("Диагональ должна принимать положительное значение")

        return diagonal_1, diagonal_2

def calculate_rhombus():
    try:
        rhombus = RhombusCreator.create_rhombus()
        rhombus.print_answer()
    except KeyboardInterrupt:
        logging.warning("Ввод прерван пользователем")
    except ValueError:
        logging.warning("Введите число")
        calculate_rhombus()
