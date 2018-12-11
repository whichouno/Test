
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

y = list(x)
print(y)

