import unittest

from shape_code.shape import Circle, Triangle


class TestCircle(unittest.TestCase):
    """
    Test of circle class.
    """
    def test_area(self):
        """
        Test area of the circle.
        """
        values_results_errors = (
            (1, 3.141592653589793),
            (3, 28.274333882308138),
            (5.2, 84.94866535306801),
        )
        for value, expected_result in values_results_errors:
            with self.subTest(
                value=value,
                expected_result=expected_result,
                msg=(
                    f'Error in calculating the area of the circle. '
                    f'With a radius of {value}, the area of the circle '
                    f'is expected to be {expected_result}.'
                ),
            ):
                result = Circle(value).area()
                self.assertEqual(result, expected_result)


class TestTriangle(unittest.TestCase):
    """
    Test of triangle class.
    """
    def test_area(self):
        """
        Test area of the triangle.
        """
        values_results_errors = (
            ((2, 3, 2), 1.984313483298443),
            ((2, 7, 8), 6.437196594791867),
            ((4.0, 3.0, 5.0), 6.0),
            ((2.0, 3.0, 5.0), 0.0),
        )
        for value, expected_result in values_results_errors:
            with self.subTest(
                value=value,
                expected_result=expected_result,
                msg=(
                    f'Error in calculating the area of the triangle. '
                    f'With sides {value}, it is expected that the area '
                    f'of the triangle will be equal to {expected_result}.'
                ),
            ):
                result = Triangle(*value).area()
                self.assertEqual(result, expected_result)

    def test_is_right_triangle(self):
        """
        Test of the "is_right_triangle" method.
        """
        triangle = Triangle(5.0, 4.0, 3.0)
        self.assertEqual(
            triangle.is_right_triangle(),
            True,
            'The "is_right_triangle" method does not work correctly.',
        )

        triangle = Triangle(1, 1, 1)
        self.assertEqual(
            triangle.is_right_triangle(),
            False,
            'The "is_right_triangle" method does not work correctly.',
        )


class TestAreAllPositiveNumbers(unittest.TestCase):
    """
    Test of the "are_all_positive_numbers" function.
    """

    def test_wrong_value(self):
        """
        Check for raising an exception with ValueError.
        """
        with self.assertRaises(ValueError) as e:
            Circle(-1)
        self.assertEqual(
            'You entered -1. Value must be greater than 0.',
            e.exception.args[0],
        )
        with self.assertRaises(ValueError) as e:
            Triangle(1, 0, 1)
        self.assertEqual(
            'You entered 0. Value must be greater than 0.',
            e.exception.args[0],
        )

    def test_wrong_type(self):
        """
        Check for raising an exception with TypeError.
        """
        with self.assertRaises(TypeError) as e:
            Circle("5")
        self.assertEqual(
            'You entered a non-numeric value.',
            e.exception.args[0],
        )
        with self.assertRaises(TypeError) as e:
            Triangle(3, '4', 5)
        self.assertEqual(
            'You entered a non-numeric value.',
            e.exception.args[0],
        )


if __name__ == "__main__":
    unittest.main()