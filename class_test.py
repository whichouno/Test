class A():
    def run(self):
        print('run...')


class a(A):
    def run(self):
        print('a run...')


def showRun(o):
    o.run()


showRun(a())


class Student(object):
    def __init__(self):
        self.aaa = 0

    @property
    def score(self):
        return self.aaa

    # @score.setter
    # def score(self,value):
    #     self.aaa = value

    @score.getter
    def xxx(self):
        return self.aaa + 1


# s = Student()
# print(s.score,s.xxx)


class Screen(object):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.resolution = 0

    @property
    def width_property(self):
        return self.width

    @width_property.setter
    def width_property(self, value):
        self.width = value

    @property
    def height_property(self):
        return self.height

    @height_property.setter
    def height_property(self, value):
        self.height = value

    @property
    def resolution_property(self):
        self.resolution = self.height * self.width
        return self.resolution


s = Screen()
s.width_property = 1024
s.height_property = 768
print(s.width)
print('resolution =', s.resolution_property)
if s.resolution_property == 786432:
    print('测试通过!')
else:
    print('测试失败!')


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().a.b.c)

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1.value)


import  uuid
print(uuid.uuid1())


