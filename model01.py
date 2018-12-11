import math


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

d = {'key': 'value'}
print(d.get('key', 'default_value'))
print(d.get('key2', 'default_value'))


sequence = [1, 2, 3, 4, 5, 6]
filtered_values = [value for value in sequence if value != 6]

print(filtered_values)

a = [5, 7, 8]
for i, index in enumerate(a):
    print("{i}{index}".format(i=i, index=index))


#列表生成器
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

G = (s.lower() for s in L1 if isinstance(s,str))
print(G)
print(next(G))
print(next(G))

def fib(count):
    n,a,b = 0,0,1
    while(n < count):
        print(b)
        a,b = b,a+b
        n= n+1

#fib(10)

def dig(count):
    i = 1
    show = True
    while(i<count):
        i = i+ 1
        show = True
        list = [ x for x in range(1,i+ 1)]
        for y in list:
            if y == i or y == 1:
                continue
            if i % y == 0:
                show = False
                break

        if(show):
            yield (i)


diglist = [x for x in dig(1000)]
print([x % 10 for x in diglist])


# for i in range(1,5):
#     print(len([o for o in filter(lambda x: int(math.log10(x))+1 == i, diglist)]))



# print(3%2,5%3,7%5,11%7,13%11,17%13,19%17)
# 5
# 21
# 143
# 1061
# 8363

# def dig_adv():
#     n = 1
#     for m in diglist:
#         if m == 1:
#             n = m
#             continue
#         # yield '%02d' % (m - n)
#         yield m - n
#         n = m
#
# digadvlist = [x for x in dig_adv()]
# print(digadvlist)

# [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# [   1, 1, 2, 2,  4,  2,  4,  2,  4,  6,  2,  6,  4,  2,  4,  6,  6,  2,  6,  4,  2,  6,  4,  6,  8]



# N = 10
# myList = [[ j for j in range(i*N-(N - 1),i*N + 1)] for i in range(1,N + 1)]
# for l in myList:
#     for d in diglist:
#         if d in l:
#             print(d)



def digX(count):
    i = 0
    show = True
    while(i<count):
        i = i+ 1
        show = True
        list = [ x for x in range(1,i+ 1)]
        for y in list:
            if y == i or y == 1:
                continue
            if i % y == 0:
                show = False
                # break

        if(show):
            yield i
        else:
            yield 0


diglist = [x for x in digX(10000)]

tmp = [ '%04d' % x for x in digX(10000)]
# tmp = [ '%04d' % x for x in diglist]
count = tmp.count('0000')
for i in range(count):
    tmp[tmp.index('0000')] = '    '

# print(tmp)



p = 10
for q in range(2,1000 + 1):
    list = [ '%03s' % y for y in tmp[q * p - p:q * p]]

    # print(len([o for o in filter(lambda x: int(math.log10(x)) + 1 == i, list)]))
    print(len(set(list)) - 1,list)


# print(int(math.log10(8))+1)



#                                         [' ', ' ', ' ', '04', ' ', '06', ' ', '08', '09']
# ['10', ' ', '12', ' ', '14', '15', '16', ' ', '18', ' ', '20', '21', '22', ' ', '24', '25', '26', '27', '28', ' ', '30', ' ', '32', '33', '34', '35', '36', ' ', '38', '39', '40', ' ', '42', ' ', '44', '45', '46', ' ', '48', '49', '50', '51', '52', ' ', '54', '55', '56', '57', '58', ' ', '60', ' ', '62', '63', '64', '65', '66', ' ', '68', '69', '70', ' ', '72', ' ', '74', '75', '76', '77', '78', ' ', '80', '81', '82', ' ', '84', '85', '86', '87', '88', ' ', '90', '91', '92', '93', '94', '95', '96', ' ', '98', '99']