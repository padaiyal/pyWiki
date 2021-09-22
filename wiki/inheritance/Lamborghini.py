from wiki.general.classes import Car


class Lamborghini(Car):

    def __init__(self):
        super(Lamborghini, self).__init__()
        self.__nitrous_on = False

    # Method overriding - Having a new definition for the method in the super class.
    def get_manufacturer(self) -> str:
        return "Lamborghini"

    def set_nitrous_state(self, nitrous_on: bool) -> None:
        self.__nitrous_on = nitrous_on

    def get_nitrous_state(self) -> bool:
        return self.__nitrous_on

    def is_speed_possible(self, speed: float) -> bool:
        # TODO: Add check to see if it nitrous, which in case the max speed will go up by 100 kmph.
        #  Try to reuse Car.is_speed_possible()
        return True


# Multilevel inheritance.
class Aventador(Lamborghini):

    def __init__(self):
        super(Aventador, self).__init__()
        self.max_speed_in_kmph = 240


if __name__ == '__main__':
    generic_car = Car()
    lamborghini = Lamborghini()
    aventador = Aventador()

    print(lamborghini.get_engine_on())
    print(generic_car.get_engine_on())
    print(aventador.get_engine_on())

    lamborghini.set_engine_on(True)
    print(lamborghini.get_engine_on())
    print(generic_car.get_engine_on())
    print(aventador.get_engine_on())

    print(lamborghini.get_manufacturer())
    # print(generic_car.get_manufacturer())
    print(aventador.get_manufacturer())

    print(lamborghini.get_max_speed_in_kmph())
    print(generic_car.get_max_speed_in_kmph())
    print(aventador.get_max_speed_in_kmph())

    # Throws an error because the engine isn't ON!
    # aventador.set_speed_in_kmph(150)

    lamborghini.set_speed_in_kmph(100)

    # TODO: Try coming up with a multiple inheritance hierarchy. What happens if two of the parent classes contain a
    #  method with the same name or a variable with the same name?
