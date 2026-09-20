from unittest import mock

regular = mock.MagicMock()
obj = mock.MagicMock(name="an object")
obj.something.return_value = 5

def do_something(o):
    return o.something(5) + 1

print(do_something(obj))

a = mock.MagicMock()
a.__str__.return_value = "hello"
print(str(a))

different_things = mock.MagicMock()
different_things.side_effect = [1, 2, 3]
print(different_things())
print(different_things())
print(different_things())