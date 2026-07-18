import unittest
from figures.hexagon_friends import HexagonFriends

class TestHexagonFriends(unittest.TestCase):
    def test_hexagon_friends_1(self):
        hexagon_friends = HexagonFriends(1)
        area = int(hexagon_friends.get_area())
        self.assertEqual(area, 6)

    def test_hexagon_friends_2(self):
        hexagon_friends = HexagonFriends(8)
        area = int(hexagon_friends.get_area())
        self.assertEqual(area, 399)

