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
            5: [0, 2, 4],
            200: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,
                  52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100,
                  102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140,
                  142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180,
                  182, 184, 186, 188, 190, 192, 194, 196, 198]
        }

        for input, expected_value in test_inputs.items():
            even_numbers_generator = even_numbers.get_even_numbers_generator(input)
            actual_output = list(even_numbers_generator)
            self.assertListEqual(expected_value, actual_output)
            # Better than self.assertEqual(expected_value, actual_output) as it provides a concise output.

        test_function: Callable[[Any, Any], list] = lambda function, *args: list(function(*args))

        self.assertRaises(AttributeError, test_function, even_numbers.get_even_numbers_generator, None)
        self.assertRaises(AttributeError, test_function, even_numbers.get_even_numbers_generator, "ijdfsiaphu")
