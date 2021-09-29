import unittest
from typing import Callable, Any

from wiki.unit_tests import even_numbers


class EvenNumberTest(unittest.TestCase):

    def test_is_even(self):
        """
        even_numbers.is_even(-2) = True
        100 = True
        0 = True
        13 = False
        -99 = False
        None = Error
        """

        test_inputs = {
            100: True,
            0: True,
            13: False,
            -99: False
        }
        for test_input, expected_output in test_inputs.items():
            self.assertEqual(expected_output, even_numbers.is_even_number(test_input))

        self.assertRaises(AttributeError, even_numbers.is_even_number, None)

        self.assertRaises(AttributeError, even_numbers.is_even_number, "wqdjgwqjqdkh")

    def test_get_even_numbers_generators(self):
        """
        None : AttributeError
        NotInt : AttributeError
        8 : 0,2,4,6
        -2 : Nothing
        0 : Nothing
        5 : 0,2,4
        """

        test_inputs = {
            8: [0, 2, 4, 6],
            -2: [],
            0: [],
            5: [0, 2, 4]
        }

        for input, expected_value in test_inputs.items():
            even_numbers_generator = even_numbers.get_even_numbers_generator(input)
            actual_output = list(even_numbers_generator)
            self.assertListEqual(expected_value, actual_output)

        test_function: Callable[[Any, Any], list] = lambda function, *args: list(function(*args))

        self.assertRaises(AttributeError, test_function, even_numbers.get_even_numbers_generator, None)
        self.assertRaises(AttributeError, test_function, even_numbers.get_even_numbers_generator, "ijdfsiaphu")
