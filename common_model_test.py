from collections import namedtuple
from collections import deque
import re, time

# --------------namedtuple-------------
point = namedtuple('point', ['x', 'y'])
p = point(1, 2)

print(p.x, p.y)

circle = namedtuple('circle', ['x', 'y', 'z'])
c = circle(1, 2, 3)

print(c.x, c.y, c.z)

# --------------deque-------------
q = deque(list(['a', 'b', 'c']))
q.append('x')
print(q)

print(dir(q))
t1 = time.time()
print(list(filter(lambda x: x if re.compile(r'^[a-zA-Z]+').match(x) else None, dir(q))))
t2 = time.time()
print('filter used time :{t:8f}'.format(t = t2- t1))


t1 = time.time()
print([x for x in dir(q) if re.compile(r'^[a-zA-Z]+').match(x)])
t2 = time.time()
print('comprehension used time :{t:8f}'.format(t = t2- t1))