import sys

x = [1,2,3,4,5,6,7]
y = map( lambda i: i**2, x )

#print(y)
#print(list(y))

print(sys.getsizeof(list(y)))
print(sys.getsizeof(y)) #smaller size
#print("*******")

for i in y:
    print(i)
#it generates the values on the fly, they are not stored in memory 
