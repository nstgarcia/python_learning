def f1(func):
    def wrapper():
        print("started")
        func()
        print("ended")
    return wrapper

def f():
    print("Hello")


#f1(f)() #returns a function object

x = f1(f)   #Same as a decorator
x()
