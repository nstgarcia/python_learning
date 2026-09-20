def f1(func):
    def wrapper(*args, **kwargs):
        print("started")
        val =func(*args, **kwargs)
        print("ended")
        return val
    return wrapper

@f1
def f(a,b):
    print(f"Hello {a} and {b}")

@f1
def add(x,y):
    return x+y

f("Nestor!", "jeje")

print( add(5,6) )
