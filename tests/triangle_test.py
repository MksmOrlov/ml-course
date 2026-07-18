import unittest
from figures.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_triangle_1(self):
        triangle = Triangle(5, 5, 5)
        perimeter = triangle.calculate_triangle_perimeter()
        self.assertEqual(perimeter, 15)

        square = triangle.calculate_triangle_square()
        self.assertEqual(square, 10.825)

    def test_triangle_2(self):
        triangle = Triangle(3, 4, 5)
        perimeter = triangle.calculate_triangle_perimeter()
        self.assertEqual(perimeter, 12)

        square = triangle.calculate_triangle_square()
        self.assertEqual(square, 6)
