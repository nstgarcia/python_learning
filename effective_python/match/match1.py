

def basic_contains_implementation(tree, value):
    if not isinstance(tree, tuple):
        return tree == value
    pivot, left, right = tree
    if value < pivot:
        return basic_contains_implementation(left, value)
    elif value > pivot:
        return basic_contains_implementation(right, value)
    else: 
        return value == pivot


my_tree = (10, (7,None,9), (13,11,None))
assert basic_contains_implementation(my_tree, 9)
assert not basic_contains_implementation(my_tree, 14)


def contains_match(tree, value):
    match tree:
        case pivot, left, _ if value < pivot:
            return contains_match(left, value)
        case pivot, _, right if value > pivot:
            return contains_match(right, value)
        case (pivot, _, _) | pivot: 
            return pivot == value

assert contains_match(my_tree, 9)
assert not contains_match(my_tree, 14)

