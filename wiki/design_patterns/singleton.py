from __future__ import annotations
from wiki.inheritance.Lamborghini import Lamborghini, Aventador


class IsaacEdition(Lamborghini):

    __onlyInstance: IsaacEdition = None

    def __init__(self):
        super(IsaacEdition, self).__init__()
        if IsaacEdition.__onlyInstance is not None:
            raise RuntimeError("Unable to instantiate more than 1 Isaac edition.")
        self.max_speed_in_kmph = 400
        IsaacEdition.__onlyInstance = self

    @staticmethod
    def get_instance() -> IsaacEdition:
        return IsaacEdition.__onlyInstance if IsaacEdition.__onlyInstance is not None else IsaacEdition()


if __name__ == '__main__':
    lamborghini1 = Aventador()
    lamborghini2 = Aventador()


    # This condition evaluates to False as both of them are separate instances.
    print(lamborghini1 == lamborghini2)

    # Instance method
    lamborghini2.get_speed_in_kmph()
    # This won't work
    # Aventador.get_max_speed_in_kmph()

    _ = IsaacEdition()
    # This won't work as IsaacEdition is a singleton.
    # isaac_edition2 = IsaacEdition()

    isaac_edition_instance1 = IsaacEdition.get_instance()
    isaac_edition_instance2 = IsaacEdition.get_instance()
    # This condition evaluates to True as both of them are the same instance.
    print(isaac_edition_instance1 == isaac_edition_instance2)

# TODO: Implement an n-ton class.
