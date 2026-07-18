import logging

from figures.figure import Figure
from figures.triangle import Triangle

logger = logging.getLogger(__name__)


class HexagonFriends(Figure):
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


class HexagonFriendsCreator:
    @staticmethod
    def create_hexagon_friends() -> HexagonFriends:
        side = HexagonFriendsCreator.get_hexagon_friends_side()
        hexagon_friends = HexagonFriends(side)
        return hexagon_friends

    @staticmethod
    def get_hexagon_friends_side() -> tuple[float]:
        side = float(input("Введите сторону причудливой фигуры: "))
        if not Figure.is_positive(side):
            side = HexagonFriendsCreator.get_hexagon_friends_side()
            logger.warning("Сторона должна принимать положительное значение")
        return side

def calculate_hexagon_friends():
    try:
        hexagon_friends = HexagonFriendsCreator.create_hexagon_friends()
        hexagon_friends.print_answer()
    except KeyboardInterrupt:
        logging.warning("Ввод прерван пользователем")
    except ValueError:
        logging.warning("Введите число")
        calculate_hexagon_friends()
