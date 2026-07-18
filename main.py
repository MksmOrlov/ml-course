from config.logging_config import setup_logging
from figures.dodecahedron import Dodecahedron
from figures.hexagon_friends import HexagonFriends
from figures.sexyangle import SexyAngle
from train.train_fly import TrainFly

setup_logging()

from figures.triangle import Triangle
from figures.rhombus import Rhombus

if __name__ == '__main__':
    # Triangle.calculate(Triangle)
    # Rhombus.calculate(Rhombus)
    # SexyAngle.calculate(SexyAngle)
    # HexagonFriends.calculate(HexagonFriends)
    # Dodecahedron.calculate(Dodecahedron)
    TrainFly.calculate(TrainFly)
