from abc import ABC, abstractmethod
from math import pi, sqrt


def are_all_positive_numbers(*nums):
    """
    Checks that all numbers are greater than zero.
    """
    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError('You entered a non-numeric value.')
        if num <= 0:
            raise ValueError(
                f'You entered {num}. Value must be greater than 0.')


class Shape(ABC):
    """
    Base class for all shapes.
    """
    @abstractmethod
    def area(self) -> float:
        """
        Calculates the area of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents the circle shape.
    """
    def __init__(self, radius: int | float):
        are_all_positive_numbers(radius)
        self._radius = radius

    def area(self) -> float:
        """
        Calculates the area of the circle.
        """
        return pi * (self._radius ** 2)

    def __str__(self):
        return f'Circle shape with a radius of {self._radius}.'


class Triangle(Shape):
    """
    Represents the triangle shape.
    """
    def __init__(
            self,
            side_a: int | float,
            side_b: int | float,
            side_c: int | float,
    ):
        are_all_positive_numbers(side_a, side_b, side_c)
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def area(self) -> float:
        """
        Calculates the area of the triangle.
        """
        try:
            s = (self._side_a + self._side_b + self._side_c) / 2
            return sqrt(s * (s - self._side_a) *
                        (s - self._side_b) *
                        (s - self._side_c))

        except ValueError:
            print('You have entered incorrect values for the sides.')

    def is_right_triangle(self) -> bool:
        """
        Checks that the triangle is right.
        """
        sides = [self._side_a, self._side_b, self._side_c]
        sides.sort()
        return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2

    def __str__(self):
        return (f'A triangle shape with sides {self._side_a}, '
                f'{self._side_b}, and {self._side_c}.')


if __name__ == '__main__':
    pass