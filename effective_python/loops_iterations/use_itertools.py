import itertools

####Type 1:linking iterators together

it = itertools.chain( [1,2,3], [4,5,6]  )
print(list(it))

# repeat

it = itertools.repeat("hello" ,3 )
print(list(it))

# cycle
# para repetir un iterator's items para siempre
it = itertools.cycle([1,2])
result = [ next(it)  for _ in range(10) ]
print(result)

noms = itertools.cycle(["nestor", "damian"])
res = [ next(noms) for _ in range(4) ]
print(res)

### Type 2: Filtering items from an iterator