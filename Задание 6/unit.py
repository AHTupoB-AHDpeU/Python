import unittest
from task3 import factorial
import timeit


class TestFactorial(unittest.TestCase):
    def setUp(self) -> None:
        print("SetUp")

    def test_factorial(self):
        time1 = timeit.default_timer()

        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertRaises(ValueError, factorial, -1)
        self.assertEqual(factorial(0), 1)
        self.assertRaises(ValueError, factorial, 21)

        time2 = timeit.default_timer()
        time_total = time2 - time1
        print("Время выполнения тестов: {:.7f} секунд!".format(time_total))

    def tearDown(self) -> None:
        print("tearDown")
