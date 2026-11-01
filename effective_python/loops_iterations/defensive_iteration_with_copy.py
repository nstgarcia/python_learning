def normalize_copy(numbers):
    numbers_copy = list(numbers) #copy the iterator
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


            
file_path="/home/n3stor/Documents/dev/repos/python_learning/effective_python/loops_iterations/my_numbers.txt"
it = read_visits(file_path)
percentages = normalize_copy(it)
print(percentages)