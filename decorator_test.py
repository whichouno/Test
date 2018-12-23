def log(func):
    def deco():
        print('call {func_name}()'.format(func_name=func.__name__))
        func()

    deco.__name__ = func.__name__
    return deco


@log
def now():
    print('2018-12-18')


# now = log(now)
# print(now.__name__)
# now()



def log2(text):
    def deco(func):
        def x():
            print('call {func_name}() {text}'.format(func_name=func.__name__, text=text))
            return func()

        return x

    return deco


@log2('hello')
def now2():
    print('2018-12-28')


# now2 = log2('hello')(now2)

# now2()


def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn


@metric
def log2(i):
    print('ok' + i)


# log2('1')



# def create():
#     return [lambda x, i = i:  i * x for i in range(5)]
#
# for mul in create():
#     print(mul(2))



