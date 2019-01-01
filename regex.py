import re

s = 'a b  c,d e;  f    g,'
news = re.split(r'[\s\,\;]+',s)
print(news)


g = re.match(r'^(\d+)(0+)$','102300').groups()
print(g)

g = re.match(r'^(\d+)(0*)$','102300').groups()
print(g)

g = re.match(r'^(\d+?)(0*)$','102300').groups()
print(g)

g = re.match(r'^(\d*)(0*)$','102300').groups()
print(g)

g = re.match(r'^(\d*)(0+)$','102300').groups()
print(g)


re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
g = re_telephone.match('010-123456').groups()
print(g)