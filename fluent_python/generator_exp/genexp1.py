import array

#to initialize tuples, arrays, and other sequences, use parenthesis instead of brackets
symbols = '$¢£¥€¤'
print("initializing a tuple")
tp =tuple(ord(symbol) for symbol in symbols )
print(tp)

print("initialing an array")


#1st parameter : defines the storage type for the numbers in the array
#2nd parameter : 
ar = array.array( 'I', (ord(symbol) for symbol in symbols ) )
print(ar)
print("********************************")

colors = ['black', 'white']
sizes= ['S', 'M', 'L']

for tshirts in ('%s %s' % (c,s) for c in colors for s in sizes ):
    print(tshirts)

print("Genexp with '{}' notation")

for tshirts in ( f'{c} ' f'{s}' for c in colors for s in sizes ):
    print(tshirts)