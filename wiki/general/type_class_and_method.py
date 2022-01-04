"""
type class and type() method
Reference: https://edube.org/learn/python-advanced-1

type(object) will return “type” by default.
"""

print(type(10))  # int
print(type("lol"))  # string

"""
By default, classes will be instances of the 'type' special class, which is the default metaclass responsible for
creating classes.

When the type() function is called with three arguments, then it dynamically creates a new class.
For the invocation of type(, , ):
* The argument specifies the class name; this value becomes the __name__ attribute of the class;
* The argument specifies a tuple of the base classes from which the newly created class is inherited; this argument 
  becomes the __bases__ attribute of the class;
* The argument specifies a dictionary containing method definitions and variables for the class body; the elements of 
  this argument become the __dict__ attribute of the class and state the class namespace.
A very simple example, when both bases and dictionary are empty, is presented below.
"""
Dog = type('Dog', (), {})

print('Type of dog: ', type(Dog))
print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

"""
As a result, we have created the simple class “Dog”.

The more complex example that dynamically creates a fully functional class is presented below.
"""


def bark(self) -> None:
    print('Woof, woof')


class Animal:
    # noinspection PyMethodMayBeStatic
    def feed(self) -> None:
        print('It is feeding time!')


Dog = type('Dog', (Animal,), {'age': 0, 'bark': bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()

"""
As you can see, the Dog class is now equipped with two methods (feed() and bark()) and the instance attribute age.
Output:
    The class name is: Dog
    The class is an instance of: <class 'type'>
    The class is based on: (<class '__main__.Animal'>,)
    The class attributes are: {'age': 0, 'bark': <function bark at 0x00000180C43E4E58>, '__module__': '__main__', 
    '__doc__': None}
    It is feeding time!
    Woof, woof

This way of creating classes, using the type function, is substantial for Python's way of creating classes using the 
class instruction:
* After the class instruction has been identified and the class body has been executed, the class = type(, , ) code is 
  executed;
* The type is responsible for calling the __call__ method upon class instance creation; this method calls two other 
  methods:
    * __new__(), responsible for creating the class instance in the computer memory; this method is run before 
      __init__();
    * __init__(), responsible for object initialization.
"""
