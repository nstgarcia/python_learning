import functools

def mult(a: int, b: int)-> int:
    return a*b

numbers = [1, 2, 3, 4, 5]
print( functools.reduce(mult,numbers) )