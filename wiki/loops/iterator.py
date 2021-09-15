from __future__ import annotations


class EvenNumberIterator:

    def __init__(self, numbers: list) -> None:
        self.numbers = numbers

    def __iter__(self) -> EvenNumberIterator:
        self.index = 0
        return self

    def __next__(self) -> int:
        while self.index < len(self.numbers) - 1 and self.numbers[self.index] % 2 != 0:
            self.index += 1
            pass

        if self.index == len(self.numbers):
            raise StopIteration

        self.index += 1
        return self.numbers[self.index - 1]


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers_iterator = EvenNumberIterator(numbers_list)
for even_number in even_numbers_iterator:
    print(even_number)

# TODO: Develop iterators to iterate a given list in the ascending or descending order.
