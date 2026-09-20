mutants

##statement deletion: entire statements are removed
#Original
def calculate_total(price, tax):
    total = price + tax
    return total
#Mutation
def calculate_total(price, tax):
    return total

### boolean switches

#Original
is_valid=True
#Mutation 
is_valid=False

### Operator replacements: swapping comparison operators
#original
if a == b:
    do_something()
#Mutation
if a != b:
    do_something()

### Arithmetic changes: 
#original
result = x+y 
#Mutation
result = x-y

### String modifications: 
#original
greeting = "Hello, World!"
#mutation
greeting ="xxHelloxx"

## Replacing expressions with None
#original 
result = function1()
#mutation
result = None

### changing array indices 
#original
value = my_list[0]
#Mutation
value = my_list[1]  

### Swapping continue with break in loops
#original 
for item in items:
    if condition:
        continue
#mutation 
for item in items:
    if condition:
        break