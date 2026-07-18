import unittest

from train.train_fly import TrainFly


class TrainFlyTest(unittest.TestCase):
    def test_train_fly(self):
        train_fly_task = TrainFly(1,1,1,2)
        fly_length = train_fly_task.calculate_fly()
        self.assertEqual(fly_length, 1)
