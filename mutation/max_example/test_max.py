from max_example.code import max_of_two
import pytest 

def test_max_of_two():
    assert max_of_two(3, 5) == 5
    assert max_of_two(10, 10) == 10
    assert max_of_two(-1, -5) == -1
