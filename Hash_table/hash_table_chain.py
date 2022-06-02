from doubely_linked_list import DLinkedList
import random

def make_hash_func(p, m):
    a = random.randint(1, p)
    b = random.randint(0, p)
    return lambda k: (((a*k + b)%p)%m)


class HashTable:

    def __init__(self, size = None):
        if type(size) != int:
            raise TypeError("Argument 'size' must be an integer number greater than zero.")
        self.__size = size
        self.list = list()
        for i in range(size):
            self.list.append(DLinkedList())
        self.__func = make_hash_func(size*11 + 1, size)

    def __getitem__(self, key):
        return self.list[key]

    def __str__(self):
        res = ''
        for i in range(self.__size):
            res += '{}: {} \n'.format(i, self.list[i])
        return res

    def __len__(self):
        return self.__size

    def get_hash(self, key):
        return self.__func(key)

    def insert(self, key):
        hash_key = self.get_hash(key)
        self.list[hash_key].insert(key)

    def find(self, key):
        hash_key = self.get_hash(key)
        return self.list[hash_key].find(key)

    def delete(self, key):
        hash_key = self.get_hash(key)
        pos = self.list[hash_key].find(key)
        if pos == None:
            raise ValueError("No such key in the table")
        self.list[hash_key].delete(pos)

ht = HashTable(10)
for i in range(1000000):
    ht.insert(i)
#print(ht)
for i in range(len(ht)):
    print("len = {}".format(len(ht[i])))
print("len = {}".format(len(ht)))
elem = ht.find(593)
print('elem = {}, 20 = {}'.format(elem, ht.find(20)))
ht.find(-1)
ht.delete(330)
#print(ht)
