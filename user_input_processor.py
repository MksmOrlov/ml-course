import logging
from abc import abstractmethod, ABC

logger = logging.getLogger(__name__)


class UserInputProcessor:
    @staticmethod
    def is_positive(number: float) -> bool:
        return number > 0

    @staticmethod
    def get_create_params(object_class, params_number: int) -> list[float]:
        params = list()
        for i in range(params_number):
            param = float(input(f"Введите значение параметра {object_class.params_name} ({(i + 1)}/{params_number}): "))
            if not UserInputProcessor.is_positive(param):
                logger.warning("Параметр должен принимать положительное значение")
                params = UserInputProcessor.get_create_params(object_class, params_number)
                break
            params.append(param)
        if not object_class.verify(params):
            logger.warning("Невозможно создать объект с заданными параметрами. Введите все параметры заново")
            params = UserInputProcessor.get_create_params(object_class, params_number)
        return params


class ObjectCalculator(ABC):
    params_number: int
    params_name: str

    @abstractmethod
    def print_answer(self) -> None:
        pass

    @staticmethod
    def verify(params: list) -> bool:
        return True

    @staticmethod
    def create(object_class, params_number: int):
        logger.info(f"Создание объекта {object_class.__name__}")
        params = UserInputProcessor.get_create_params(object_class, params_number)
        obj = object_class(*params)
        return obj

    @staticmethod
    def calculate(object_class):
        try:
            obj = ObjectCalculator.create(object_class, object_class.params_number)
            obj.print_answer()
        except KeyboardInterrupt:
            logging.warning("Ввод прерван пользователем")
            exit()
        except ValueError:
            logging.warning("Введите число")
            ObjectCalculator.calculate(object_class)
