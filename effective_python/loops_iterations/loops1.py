names = ["Cecilia","Lise", "Marie"]
counts = [len(n) for n in names]
print(f"counts: {counts}")

longest_name = None
max_count =0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)
print("*******Trying better approach with enumerate *******")
longest_name =None
max_count=0

for i, name in enumerate(names):#changed
    count = counts[i]    
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

print("*********Trying better approach with zip *******************************")

longest_name = None
max_count =0

for name, count in zip(names, counts):
    print(f"name: {name}")
    print(f"count: {count}")
    if count > max_count:
        longest_name = name 
        max_count = count
print(longest_name)

print("********** Checking how zip handles different lengths")

names.append("Rosalind")

for name, count in zip(names, counts):
    print(name)

print("******checking if there's any exception while using zip*****")
for name, count in zip(names, counts, strict=True):
    print(name)