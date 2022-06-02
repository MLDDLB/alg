from queue import LifoQueue

mystack = LifoQueue()

mystack.put('a')
mystack.put('b')
mystack.put('c')

print("mystack = {}".format(mystack))

print("1 = {}, 2 = {}, 3 = {}".format(mystack.get(), mystack.get(), mystack.get()))
