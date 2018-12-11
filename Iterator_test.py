from collections import Iterable, Iterator

#可迭代对象(Iterable)：可用于for循环的对象。
#迭代器(Iterator)：可用于next()调用返回下一个值的对象。



l = [1,2,3,4,5]
g = (x for x in l)

print('-------------迭代对象---------------')
print("Type of l is:{0}".format(type(l)))
print("Type of g is:{0}".format(type(g)))

print("Is l is Iterable:{0}".format(isinstance(l,Iterable)))
print("Is p is Iterable:{0}".format(isinstance(g,Iterable)))

print('-------------迭代器---------------')
print("Is l is Iterator:{0}".format(isinstance(l,Iterator)))
print("Is p is Iterator:{0}".format(isinstance(g,Iterator)))


#Iterabled对象(非Iterator)可通过iter()转换为Iterator
print('-------------迭代对象 转 迭代器---------------')
print("Is l is Iterator:{0}".format(isinstance(iter(l),Iterator)))
print("Is p is Iterator:{0}".format(isinstance(g,Iterator)))

print('-------------for循环---------------')

#for循环实现next()完成对Iterator的迭代
for x in l:
    print(x)

print('-------------next()循环---------------')

it = iter(l)

print(it)
print(list(it))

while(True):
    try:
        #it为迭代器。
        x = next(it)
        #x = next(iter(l)) Error!!! 每次循环都产生新的迭代器。
        print(x)
    except StopIteration:
        break;