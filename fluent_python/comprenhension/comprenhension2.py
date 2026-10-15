#example 2-4

#cartesian product using a list comprenhension
colors = ['black', 'white']
sizes = ['S', 'M','L']
print("tuples arranged by color, then sizes ")
tshirts =[ (color,size) for color in colors for size in sizes ]
print(tshirts)


print("resulting list is arranged as if the for loops were nested")
for color in colors:
    for size in sizes:
        print( (color,size))


print("items arranged by size, then color")
tshirts = [ (color, size)   for size in sizes 
                            for color in colors]

print(tshirts)