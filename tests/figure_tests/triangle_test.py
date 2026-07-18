import unittest
from figures.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_triangle_1(self):
        triangle = Triangle(5, 5, 5)
        perimeter = triangle.get_perimeter()
        self.assertEqual(perimeter, 15)

        area = int(triangle.get_area())
        self.assertEqual(area, 10)

    def test_triangle_2(self):
        triangle = Triangle(3, 4, 5)
        perimeter = triangle.get_perimeter()
        self.assertEqual(perimeter, 12)

        area = triangle.get_area()
        self.assertEqual(area, 6)
