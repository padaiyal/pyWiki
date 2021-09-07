import time


class Car:
    """
    Abstracts a car. It is meant to have all the functionalities of an actual car.
    """

    def __init__(self) -> None:
        self.__engine_on: bool = False
        self.__speed_in_kmph: float = 0

    def set_engine_on(self, engine_on: bool) -> None:
        """
        Set the state of the engine.
        :param engine_on: Engine state as a boolean value. If True, it means the engine is ON, else it is OFF.
        """
        self.__engine_on = engine_on

    def get_engine_on(self) -> bool:
        """
        Get the state of the engine.
        :return: True if engine is ON, else False.
        """
        return self.__engine_on

    def set_speed_in_kmph(self, speed_in_kmph: float) -> None:
        """
        Set speed of the car in kmph.
        :param speed_in_kmph: Speed of car in kmph.
        """
        # TODO: Input validation. Check if the speed_in_kmph variable contains valid values.
        if not self.__engine_on:
            raise AttributeError("Cannot set speed when engine isn't ON!")
        self.__speed_in_kmph = speed_in_kmph

    def get_speed_in_kmph(self) -> float:
        """
        Get the speed of the car in kmph.
        :return: The speed of the car in kmph.
        """
        return self.__speed_in_kmph


car1: Car = Car()
print(car1.get_engine_on())
print(car1.get_speed_in_kmph())

# car.set_speed_in_kmph(100) # Raises an error as car speed cannot be set when engine isn't ON.

car1.set_engine_on(True)
car1.set_speed_in_kmph(100)
print(car1.get_engine_on())
print(car1.get_speed_in_kmph())

car2: Car = Car()
print(car2.get_engine_on())
print(car2.get_speed_in_kmph())


time.sleep(1)
"""
TODO: Add functionality to brake. Braking reduces the speed by 5kmph per second. Two brake methods. 
One to got to desired speed. Another to brake for specified duration.
"""
