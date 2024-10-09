import unittest
from prime import prime

class TestPrime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(prime(2))
        self.assertTrue(prime(3))
        self.assertTrue(prime(5))
        self.assertTrue(prime(7))
        self.assertTrue(prime(11))
        self.assertTrue(prime(13))
        self.assertTrue(prime(17))
        self.assertTrue(prime(19))
        self.assertTrue(prime(23))
        self.assertTrue(prime(29))
        
    def test_not_prime(self):
        self.assertFalse(prime(0))
        self.assertFalse(prime(4))
        self.assertFalse(prime(6))
        self.assertFalse(prime(8))
        self.assertFalse(prime(9))
        self.assertFalse(prime(10))
        self.assertFalse(prime(12))
        self.assertFalse(prime(14))
        self.assertFalse(prime(15))
        self.assertFalse(prime(16))
        self.assertFalse(prime(18))
        self.assertFalse(prime(20))
        self.assertFalse(prime(21))
        self.assertFalse(prime(22))
        self.assertFalse(prime(24))
        self.assertFalse(prime(25))
        self.assertFalse(prime(26))
        self.assertFalse(prime(27))
        self.assertFalse(prime(28))
        self.assertFalse(prime(30))

if __name__ == '__main__':
    unittest.main()