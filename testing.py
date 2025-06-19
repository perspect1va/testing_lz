from testing_lz import gang
from testing2 import gang_man_tests
import unittest

#Автомат тесты
class Test_Equalize(unittest.TestCase):

    def test_valid_1(self):
        self.assertAlmostEqual(gang(2, 3, 4), 0.30694266481558556, places=6)

    def test_valid_2(self):
        self.assertAlmostEqual(gang(5, 2, 1), 1.448147589853455, places=6)

    def test_log_domain_error(self):
        with self.assertRaises(ValueError):
            gang(0.5, 2, 1)

    def test_div_zero_1(self):
        with self.assertRaises(ZeroDivisionError):
            gang(3, 2, 4)

    def test_div_zero_2(self):
        with self.assertRaises(ZeroDivisionError):
            gang(10, 5, 5)

    def test_sqrt_domain_error(self):
        with self.assertRaises(ValueError):
            gang(1, 2, 3)

if __name__ == '__main__':
    gang_man_tests()
    print("Автоматическое тестирование:\n")
    unittest.main()    
