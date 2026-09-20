import sys

def gen(n):
    for i in range(n):
        yield i

for i in gen(5):
    print(i)

#same but manually

x = gen(5)

print(next(x))
print(next(x))

print("#############")

def gen():
    yield 1
    print('Pause 1')
    yield 2
    print('Pause 2')
    yield 3
    print('Pause 3')
    yield 4

x = gen()
print(next(x))
print(next(x))