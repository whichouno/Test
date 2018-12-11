#杨辉三角生成器
def triangles():
    lineindex = 1
    list = []
    while (True):
        if lineindex == 1:
            list = [1]
        elif lineindex == 2:
            list = [1, 1]
        else:
            list_len = len(list)
            list = [1] + [list[i] + list[i + 1] for i in range(list_len - 1)] + [1]
        yield list
        lineindex = lineindex + 1

#生成器单步调用

t = triangles()
print(next(t))
print(next(t))
print(next(t))

print('----------------------------')

#生成器循环调用
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

print('----------------------------')
#两个for循环为嵌套关系
# list = [1,2,3,4,5]
# print([x + y for x in list[:-1] for y in list[1:]])
# for x in list[:-1]:
#     print(x)

