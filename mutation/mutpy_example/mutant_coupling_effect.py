

#def abs_diff(a, b):
#    if a > b:
#        return a - b
#    else:
#        return b - a

#def abs_diff(a, b):
#    if a < b:  # mutant A: operator replacement
#        return a - b
#    else:
#        return b - a

def abs_diff(a, b):
    if a > b:
        return b - a  # mutant B: reverse substraction
    else:
        return a - b


#Test suite
def test_abs_diff():
    assert abs_diff(5, 3) == 2  #test 1
    assert abs_diff(3, 5) == 2  #test 2
    assert abs_diff(4, 4) == 0  #test 3

### Test 1 kills mutant A and B. 