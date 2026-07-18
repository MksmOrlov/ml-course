import unittest
from figures.dodecahedron import Dodecahedron

class TestDodecahedron(unittest.TestCase):
    def test_dodecahedron_1(self):
        dodecahedron = Dodecahedron(1)
        area = round(dodecahedron.get_area(), 2)
        self.assertEqual(area, 20.65)

    def test_dodecahedron_2(self):
        dodecahedron = Dodecahedron(2)
        area = round(dodecahedron.get_area(), 2)
        self.assertEqual(area, 82.58)

