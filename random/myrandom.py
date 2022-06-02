import time
import random

'''def random(a, b):
    t1 = time.time_ns()//100
    flag = None
    if t1 % 2 == 0:
        flag = 1
    else:
        flag = 0
    if b == a:
        return a
    elif b > a:
        t2 = time.time_ns()//200
        if flag == 1:
            return ((t1 + t2) % b + a)
        else:
            return ((t1 + t2) % (b + 1) + a)
    elif a > b:
        t2 = int(time.time())
        if flag == 1:
            return ((t1 + t2) % a + b)
        else:
            return ((t1 + t2) % (a + 1) + b)'''

a = 3
b = 7
ls = list()
for i in range(a, b):
    ls.append(random.randrange(0, 64))
print("list = {}".format(ls))
