import sys

x = [1,2,3,4,5,6,7]
y = map( lambda i: i**2, x )

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print("ooo")

for i in y:
    print(i)