#! python

from calculator import add, subtract, multiply, divide, power
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 5

    def tearDown(self):
        self.a = None
        self.b = None

    def test_add_positive(self):
        self.assertEqual(add(self.a, self.b), 15)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_subtract_positive(self):
        self.assertEqual(subtract(self.a, self.b), 5)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 7), -4)

    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 7), 21)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(self.a, 0), 0)

    def test_divide_positive(self):
        self.assertEqual(divide(self.a, self.b), 2)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(self.a, 0)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)