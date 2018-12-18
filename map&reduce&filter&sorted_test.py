from functools import reduce

l = ['adam', 'LISA', 'barT']
def normalize(name):
    # def change_name(name):
    #     newname = name[0].upper() + name[1:].lower()
    #     return newname
    # return map(change_name, name)
    return map((lambda name:name[0].upper() + name[1:].lower()),name)

x = normalize(l)
print(next(x))
print(next(x))
print(next(x))

x = normalize(l)
y = list(x)
print(y)




def prod(L):
    return reduce((lambda x,y:x*y),L)


print(prod([3, 5, 7, 9]))





def _not_divisible(n):
    return lambda x: x % n > 0

def odd_iter():
    n = 1
    while(True):
        n = n + 2
        yield n


def primes():
    it = odd_iter()
    while(True):
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
        #filter 遍历第二个参数（迭代器），直到遍历完或者遇到符合条件的元素，则返回空迭代器或返回相当于修改规则的新迭代器
        # print(next(it))
        # print(next(it))

for x in primes():
    if x < 15:
        pass
        # print(x)
    else:
        break
#
# print(list(it))


g = (x for x in range(0))

print(g)


ss = filter(lambda x : x > 10, g)
print(list(ss))
# print(next(g))


# def is_odd(n):
#     return lambda x: x - n == 6
#
# it = odd_iter()
# # print(next(it))
#
# it2 = filter(is_odd(1), it)
# print(next(it2))


def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(list(filter(is_palindrome,range(1,1000))))




print(sorted([1,-1,2,8,3,-10],key=abs))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L = [{'Bob', 75}, {'Adam', 92}, {'Bart', 66}, {'Lisa', 88}]


def by_name(t):
    return t[0]

print(sorted(L,key=by_name))
print(sorted(L,key=(lambda x : x)))


#
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f(i):
#             def g():
#                 return i*i
#             return g
#         fs.append(f(i))
#     return fs


def count():
    fs = []
    for i in range(1, 4):
        fs.append((lambda i : lambda : i*i)(i))
    return fs


f1, f2, f3 = count()

print(f1(),f2(),f3())


# def get_y(a,b):
#     def func(x):
#         return a * x+b
#     return func
# y1 = get_y(1,1)
# print(y1(1))


def createCounter():
    i = 0
    def counter():
        nonlocal i
        i = i + 1
        return i
    return counter


cA = createCounter()
print(cA(),cA())


L = list(filter((lambda x : True if x % 2 == 1 else False),range(1,20)))
print(L)