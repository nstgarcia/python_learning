

class Node:
    def __init__(self,value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

obj_node = Node(value=10,
                left=Node(value=7, right=9),
                right=Node(value=13, left=11),
                )

def contains_class(tree, value):
    if not isinstance(tree, Node):
        return tree == value
    if value < tree.value:
        return contains_class(tree.left, value)
    elif value > tree.value:
        return contains_class(tree.right, value)
    else:
        return value == tree.value

def contains_match_with_class(tree, value):
    match tree:
        case Node(value=pivot, left=left) if value < pivot:
            return contains_match_with_class(left, value)
        case Node(value=pivot, right=right) if value > pivot:
            return contains_match_with_class(right, value)
        case Node(value=pivot) | pivot:
            return pivot == value

assert contains_match_with_class(obj_node, 7)
assert not contains_match_with_class(obj_node, 14)

assert contains_class(obj_node, 7)
assert not contains_class(obj_node, 14)