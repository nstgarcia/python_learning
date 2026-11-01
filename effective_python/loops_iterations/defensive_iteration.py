def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15,35,80]
percentages = normalize(visits)
print(f"Printing percentages: \n{percentages}")

print("\nnow checking that a generator gets exhausted\n")

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

file_path="/home/n3stor/Documents/dev/repos/python_learning/effective_python/loops_iterations/my_numbers.txt"
it = read_visits(file_path)
#the iterator is in "it" and once it's read the first time, it gets exhausted
percentages = normalize(it)
print(percentages)


file_path="/home/n3stor/Documents/dev/repos/python_learning/effective_python/loops_iterations/my_numbers.txt"
it = read_visits(file_path)
print(list(it))
print(list(it)) #already exhausted