from config.logging_config import setup_logging

setup_logging()

from figures.triangle import calculate_triangle
from figures.rhombus import calculate_rhombus


if __name__ == '__main__':
    calculate_triangle()
    calculate_rhombus()
