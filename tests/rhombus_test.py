import unittest
from figures.rhombus import Rhombus

class TestRhombus(unittest.TestCase):
    def test_rhombus_1(self):
        rhombus = Rhombus(2, 10)
        area = rhombus.get_area()
        self.assertEqual(area, 10)

    def test_rhombus_2(self):
        rhombus = Rhombus(3.6, 7.6)
        area = rhombus.get_area()
        self.assertEqual(area, 13.68)
