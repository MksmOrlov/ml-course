import logging

from user_input_processor import ObjectCalculator

logger = logging.getLogger(__name__)


# [===] ->       *_*        <- [===]
# поезд_1        муха         поезд_2
class TrainFly(ObjectCalculator):
    params_number = 4
    params_name = "Расстояние, скорость поезда 1, скорость поезда 2, скорость мухи"

    def __init__(self, length: float, velocity_train_1: float, velocity_train_2: float, velocity_fly: float):
        self._length = length # Расстояние L км между поездами
        self._velocity_train_1 = velocity_train_1 # Скорость v1 км/ч первого поезда
        self._velocity_train_2 = velocity_train_2 # Скорость v2 км/ч второго поезда
        self._velocity_fly = velocity_fly # Скорость vm км/ч мухи
        
        self._length_fly = None

    @staticmethod
    def verify(params: list) -> bool:
        if not (params[3] > params[1] and params[3] > params[2]):
            logger.warning("По условию задачи, муха должна быть быстрее любого из поездов")
            return False
        return True
    
    def calculate_fly(self) -> float:
        """Считаем, сколько времени проживет муха (расстояние между поездами делить на общая скорость поездов) и умножаем время мухи на скорость мухи"""
        if self._length_fly:
            return self._length_fly
        total_velocity = self._velocity_train_1 + self._velocity_train_2
        fly_time_to_live = self._length / total_velocity

        self._length_fly = fly_time_to_live * self._velocity_fly
        return self._length_fly

    def print_answer(self) -> None:
        length_fly = self.calculate_fly()
        logger.info(f"Муха успеет пролететь до столкновения поездов {length_fly} км")
