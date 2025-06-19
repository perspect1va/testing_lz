from testing_lz import gang
from testing2 import gang_man_tests
import unittest

class Test_Equalize(unittest.TestCase):
    def test_valid_1(self):
        result = gang(2, 3, 1)
        if isinstance(result, str):
            self.fail(f"Ожидалось число, получена ошибка: {result}")
        self.assertAlmostEqual(result, 0.24012907173427356, places=6)

    def test_valid_2(self):
        result = gang(5, 2, 1)
        if isinstance(result, str):
            self.fail(f"Ожидалось число, получена ошибка: {result}")
        self.assertAlmostEqual(result, 1.448147589853455, places=6)

    def test_log_domain_error(self):
        result = gang(0, 2, 1)
        self.assertIsInstance(result, str)
        self.assertIn("", result)
           
    def test_div_zero_1(self):
        result = gang(2, 2, 2)
        self.assertIsInstance(result, str)
        self.assertIn("Ошибка при вычислении: Знаменатель левого члена равен 0", result)

    def test_sqrt_domain_error(self):
        result = gang(1, 2, 3)
        self.assertIsInstance(result, str)
        self.assertIn("Выражение под корнем должно быть положительным", result)

if __name__ == '__main__':
    gang_man_tests()
    print("Автоматическое тестирование:\n")
    unittest.main()