path = '/Users/ouno/Project/test/file1'

with open(path,'r') as f:
    s = f.read()
    # print(s)



from io import StringIO
import os

f = StringIO()
f.write('12345')

f.seek(0)
print(f.read())



print(os.path.abspath('.'))




# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


import pickle

# i = 101
# b = pickle.dumps(i)
# f = open('dump.txt','wb')
# pickle.dump(b,f)
# f.close()


f2 = open('dump.txt','rb')
d = pickle.load(f2)
f2.close()

print(pickle.loads(d),type(pickle.loads(d)))