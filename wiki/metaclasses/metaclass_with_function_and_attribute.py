from __future__ import annotations
from datetime import datetime

"""
Estimated time
45 minutes

Level of difficulty
Medium

Objectives
 - improving the student's skills in operating with meta classes;
 - improving the student's skills in operating with class variables and class methods.

Scenario
    Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated 
    as legacy code;
    the system was created by a group of volunteers who worked with no clear “clean coding” rules;
    the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple 
    dependency problems;
    your task is to prepare a metaclass that is responsible for:
    equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
    equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the 
    value of the class attribute instantiation_time.
    * The metaclass should have its own class variable (a list) that contains a list of the names of the classes 
    instantiated by the metaclass (tip: append the class name in the __new__ method).

Your metaclass should be used to create a few distinct legacy classes;
create objects based on the classes;
list the class names that are instantiated by your metaclass.
"""


class MetaClass(type):
    classes = list()

    def __new__(mcs, name, bases, dictionary) -> MetaClass:
        MetaClass.classes.append(name)

        def get_instantiation_time(self):
            return self.instantiation_time

        dictionary['get_instantiation_time'] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = datetime.now()
        print(type(obj))
        return obj


class LegacyClass1(metaclass=MetaClass):
    pass


class LegacyClass2(metaclass=MetaClass):
    pass


class NewClass(metaclass=type):
    pass


if __name__ == '__main__':
    legacyClass1Object = LegacyClass1()
    legacyClass2Object = LegacyClass2()
    newClassObject = NewClass()

    print(MetaClass.classes)

    # noinspection PyUnresolvedReferences
    print(legacyClass1Object.get_instantiation_time())
    # noinspection PyUnresolvedReferences
    print(legacyClass2Object.get_instantiation_time())
    # The following statement will error out as the NEwClass doesn't have the meta class that will provide the function.
    # print(newClassObject.get_instantiation_time())
