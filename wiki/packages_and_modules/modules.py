# modules are files that contain python code.
# from <module> import <class>, <function>, <variable>
# from classes import Car  # Here, we are importing the Car class from the classes module.
from time import time  # Here, we are importing the time() function from the time module.

# noinspection PyUnresolvedReferences
from python_script import add # Does not execute the contents within the if block checking for the the module name as
# '__main__'
# noinspection PyUnresolvedReferences
from python_not_a_script import add

time()
# car1 = Car()
