# import required libraries
from unittest import TestCase
from src.isPrime import isPrime
#mut.py --target src.isPrime --unit-test test_prime -m --runner pytest

# define a class
class CalculatorTest(TestCase):
    
    # test case for checking non prime nums
    def test_nonprime(self):
        self.assertEqual(isPrime(12),False)
    
    # test case to check prime nums
    def test_prime(self):
        self.assertEqual(isPrime(19),True)

    # test case to check invalid input
    def test_invalid(self):
        self.assertEqual(isPrime(-1),False)

        
    def test_isPrime(self):
        # Test for prime numbers
        assert isPrime(2) == True
        assert isPrime(3) == True
#        assert isPrime(13) == True
#
#        # Test for non-prime numbers
#        assert isPrime(1) == False
#        assert isPrime(4) == False
        assert isPrime(0) == False
#        assert isPrime(-5) == False
#        assert isPrime(9) == False
#
#        # Test for mutant "if not (num > 1)"
#        # This test will fail if the mutant is present
#        #assert isPrime(2) == True  # 2 is a prime number