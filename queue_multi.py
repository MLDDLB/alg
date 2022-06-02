from queue import Queue

myQueue = Queue()

myQueue.put('a')
myQueue.put('b')
myQueue.put('c')

print(myQueue)

print("1 = {}, 2 = {}, 3 ={}".format(myQueue.get(), myQueue.get(), myQueue.get()))
