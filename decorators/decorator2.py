def f1(func):
    def wrapper(*args, **kwargs):
        print("started")
        func(*args, **kwargs)
        print("ended")
    return wrapper

@f1
def f(a,b):
    print(f"Hello {a} and {b}")

f("Nestor!", "jeje")