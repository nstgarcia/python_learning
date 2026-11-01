for i in range(3):
    print(f"inside {i=}")
print(f"after {i=}")

categories = ["Hydrogen","Uranium","Iron","Other"]
#categories = []
for y, name in enumerate(categories):
    if name == "Iron":
        break
print(y)

print("****** now use comprehensions")

my_numbers = [37,13,128,21]
found = [i for i in my_numbers if i%2 == 0]
print(i)