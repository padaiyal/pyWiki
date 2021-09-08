import time


class Car:
    """
    Abstracts a car. It is meant to have all the functionalities of an actual car.
    """

    def __init__(self) -> None:
        self.engine_on: bool = False
        self.speed_in_kmph: float = 0

    def set_engine_on(self, engine_on: bool) -> None:
        """
        Set the state of the engine.
        :param engine_on: Engine state as a boolean value. If True, it means the engine is ON, else it is OFF.
        """
        self.engine_on = engine_on

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
        if speed_in_kmph < 0:
            raise AttributeError("Can't set the speed to a negative value.")

        if not self.__engine_on:
            raise AttributeError("Cannot set speed when engine isn't ON!")
        self.speed_in_kmph = speed_in_kmph

    def get_speed_in_kmph(self) -> float:
        """
        Get the speed of the car in kmph.
        :return: The speed of the car in kmph.
        """
        return self.speed_in_kmph

    """
    TODO: Add functionality to brake. Braking reduces the speed by 5kmph per second. Two brake methods. 
    One to got to desired speed. Another to brake for specified duration.
    """

    def brake_to_speed(self, desired_speed: float ) -> None :
        """
        Brake at a rate of 5kmph/s until the car is at the desired speed.
        Desired_speed: Is the speed at which you want the car to be. 
        """
        if desired_speed > self.speed_in_kmph:
            raise AttributeError("Cannot brake to a higher speed")
        
        if desired_speed < 0 :
            desired_speed = 0

        while self.speed_in_kmph - desired_speed != 0:

          if self.speed_in_kmph - desired_speed > 5:
              self.speed_in_kmph -= 5
              time.sleep(0.9999999999)
        
          else:
              self.speed_in_kmph = self.speed_in_kmph - desired_speed
              time.sleep(0.9999999)


    def brake_for(self, time: int ) -> None:
        """
        Brake at a rate of 5kmph/s for a certain duration.
        Time: Is the duration for which you want to brake. 
        """

        for second in range(time): 

          if self.speed_in_kmph >= 5:
              self.speed_in_kmph -= 5
              time.sleep(0.9999999999)
        
          else:
              self.speed_in_kmph = 0
              time.sleep(0.9999999)
              break
        



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

