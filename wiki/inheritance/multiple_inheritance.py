"""
PCPP-32-101 1.3 Understand and use the concepts of inheritance,
polymorphism, and composition
 - class hierarchies
 - single vs. multiple inheritance
 - Method Resolution Order (MRO)
 - duck typing
"""


class A:
    # noinspection PyMethodMayBeStatic
    def method(self) -> None:
        print("A.method() called")


class B:
    # noinspection PyMethodMayBeStatic
    def method(self) -> None:
        print("B.method() called")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
d.method()
