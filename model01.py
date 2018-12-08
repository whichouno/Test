s = set(['a', 'b', 'b'])


def lookup_set(s):
    return 'a' in s


print(lookup_set(s))


def Foot(attr):
    if attr:
        print('True')
    else:
        print('None')



def fun(x):
    return x+1

def test_answer():
    assert fun(3) == 5

