import unittest

d = {'key': 'value'}
print(d.get('key', 'default_value'))
print(d.get('key2', 'default_value'))


sequence = [1, 2, 3, 4, 5, 6]
filtered_values = [value for value in sequence if value != 6]

print(filtered_values)

a = [5, 7, 8]
for i, index in enumerate(a):
    print("{i}{index}".format(i=i, index=index))


def fun(x):
    return x+1


def test_answer():
    assert fun(1) == 2
    assert fun(2) == 3
    assert fun(3) == 4
    assert fun(4) == 5

# add annotation

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)


def square(x):
    """
    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
