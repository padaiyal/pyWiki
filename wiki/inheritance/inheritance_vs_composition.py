"""
PCPP-32-101 1.3 Understand and use the concepts of inheritance,
polymorphism, and composition
 - inheritance vs. composition
 - modelling real-life problems using the "is a" and "has a" relations

Inheritance models what is called an is a relationship. This means that when you have a Derived class that inherits
from a Base class, you created a relationship where Derived is a specialized version of Base.
Inheritance is to be used whenever the behavior of a class needs to be changed or extended.

Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of
other types. This means that a class Composite can contain an object of another class Component. This relationship
means that a Composite has a Component.
Composition is to be used when the class's behavior is to be used as is but attribute values are different.

References:
     - https://realpython.com/inheritance-composition-python/
"""
from abc import abstractmethod


class LivingBeing:
    def __init__(self, age: int):
        self.age: int = age

    def get_age(self) -> int:
        return self.age


class Whale(LivingBeing):
    def __init__(self):
        super(Whale, self).__init__(150)

    def swim(self) -> None:
        print("Swimming ...")


class Human(LivingBeing):
    def __init__(self):
        super(Human, self).__init__(100)

    def swim(self) -> None:
        print("Swimming ...")

    def walk(self) -> None:
        print("Walking ...")


if __name__ == '__main__':
    """
    These can be used to represent a human and whale respectively only for attributes like age. The ease of
    representation comes with a price of not having custom behavior/methods like inheritance.
    """
    living_being_1: LivingBeing = LivingBeing(100)
    living_being_2: LivingBeing = LivingBeing(150)
    print(living_being_1.get_age())
    print(living_being_2.get_age())

    human_obj: Human = Human()
    whale_obj: Whale = Whale()
    print(human_obj.get_age())
    human_obj.swim()
    human_obj.walk()

    print(whale_obj.get_age())
    whale_obj.swim()
    # This will throw an error as the whale doesn't have walk().
    # whale_obj.walk()


