from __future__ import annotations
"""
Metaclass

Metaclass is a class whose instances are classes. Just as an ordinary class defines the behavior of certain objects, a
metaclass allows for the customization of class instantiation.

Metaclasses usually implement these two methods (__init__, __new__), taking control of the procedure of creating and
initializing a new class instance. Classes receive a new layer of logic.

The typical use cases for metaclasses:
* logging;
* registering classes at creation time;
* interface checking;
* automatically adding new methods;
* automatically adding new variables.

Now that we know what’s happening under Python's hood, it’s time to implement our own metaclass.
It’s important to remember that metaclasses are classes that are instantiated to get classes.

The first step is to define a metaclass that derives from the type 'type' and arms the class with a 'custom_attribute',
as follows.
"""


class MyMeta(type):
    def __new__(mcs, name, bases, dictionary) -> MyMeta:
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj


"""
Pay attention to the fact that:
* the class My_Meta is derived from type. This makes our class a metaclass;
* our own __new__ method has been defined. Its role is to call the __new__ method of the parent class to 
create a new class;
* __new__ uses 'mcs' to refer to the class – it’s just a convention;
* a class attribute is created additionally;
* the class is returned.
Let's make use of the metaclass to create our own, domain-specific class, and check if it’s armed with the custom 
attribute:

"""


class MyObject(metaclass=MyMeta):
    pass


print(MyObject.__dict__)

"""
Pay attention to the fact that:
* A new class has been defined in a way where a custom metaclass is listed in the class definition as a metaclass. This 
is a way to tell Python to use My_Meta as a metaclass, not as an ordinary superclass;
* We are printing the contents of the class __dict__ attribute to check if the custom attribute is present.

Output:
    {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'My_Object' objects>, '__weakref__': <attribute 
    '__weakref__' of 'My_Object' objects>, '__doc__': None, 'custom_attribute': 'Added by My_Meta'}

Indeed, the class attribute has been created.
Let's run a more serious experiment: try to build a metaclass responsible for completing classes with a method (if 
missing) to ensure that all your classes are equipped with a method named 'greetings'.
"""


# noinspection PyUnusedLocal
def greetings(self) -> None:
    print('Just a greeting function, but it could be something more serious like a check sum')


class MyMeta1(type):
    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj


class MyClass1(metaclass=MyMeta1):
    pass


class MyClass2(metaclass=MyMeta1):
    # noinspection PyMethodMayBeStatic
    def greetings(self) -> None:
        print('We are ready to greet you!')


myObj1 = MyClass1()
myObj1.greetings()
myObj2 = MyClass2()
myObj2.greetings()
