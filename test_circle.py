"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle


# TODO write 3 tests as described above
class CircleTest(unittest.TestCase):
    """Tests of the Circle  class."""

    def test_add_area_positive(self):
        """test for add_area using typical values."""
        circle1 = Circle(radius=3)
        circle2 = Circle(radius=5)
        circle_area = circle1.add_area(circle2).get_area()
        expected_area = circle1.get_area() + circle2.get_area()
        self.assertAlmostEqual(circle_area, expected_area)

    def test_add_area_zero(self):
        """test for add_area for an "edge case" where one circle has radius 0."""
        circle1 = Circle(radius=0)
        circle2 = Circle(radius=5)
        circle_area = circle1.add_area(circle2).get_area()
        expected_area = circle1.get_area() + circle2.get_area()
        self.assertAlmostEqual(circle_area, expected_area)

    def test_add_area_exception(self):
        """test that circle constructor raises exception of radius is negative."""
        with self.assertRaises(ValueError):
            Circle(radius=-1)


if __name__ == '__main__':
    unittest.main()
