import unittest
from figures.sexyangle import SexyAngle

class TestSexyAngle(unittest.TestCase):
    def test_sexyangle_1(self):
        sexyangle = SexyAngle(1)
        area = sexyangle.get_area()
        self.assertEqual(area, 4.763)

    def test_sexyangle_2(self):
        sexyangle = SexyAngle(85)
        area = sexyangle.get_area()
        self.assertEqual(area, 34413.685)
