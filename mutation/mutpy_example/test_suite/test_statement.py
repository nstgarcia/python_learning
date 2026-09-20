#from statement import add_numbers, multiply_numbers
from src.statement import add_numbers

import pytest 

#mut.py --target src.statement --unit-test test_statement -m --runner pytest


def test_add_numbers():
    assert add_numbers(2, 3) == 5

#def test_add_numbers_negative():
#    assert add_numbers(2, 3) != -1
#
#    

#def test_multiply_numbers():
#    assert multiply_numbers(2, 3) == 6