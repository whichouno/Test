import unittest

def fun(x):
    return x+1


def test_answer():
    assert fun(1) == 2
    assert fun(2) == 3
    assert fun(3) == 4
    assert fun(4) == 3

# add annotation

class MyTest(unittest.TestCase):
    def setUp(self):
        pass#print('setUp...')

    def tearDown(self):
        pass#print('tearDown...')

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


#unittest.main(verbosity=3, exit=False)

print('1')

def create_multipliers():
    return [lambda x : i * x for i in range(5)]


for i in create_multipliers():
    print(i(1))

if __name__ == '__main__':
    #unittest.main()
    print('2')
    import doctest
    doctest.testmod()
    print('3')