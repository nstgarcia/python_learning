from src.fiz import fizzbuzz
import pytest 

#mut.py --target src.fiz --unit-test test_fiz -m --runner pytest

def test_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"


#def test_number():
#    assert fizzbuzz(7) == "7"