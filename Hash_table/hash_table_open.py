import random

def make_hash_func(m):
    return lambda k, i: (k%m + i*(1 + k%(m-1)))%m

class HashTable:

    def __init__(self, size):
        if type(size) != int:
            raise TypeError("Argument 'size' must be an integer number greater than zero.")
        self.__size = size
        self.list = [None for i in range(size)]
        self.__func = make_hash_func(size)

    def __getitem__(self, key):
        return self.list[key]

    def __str__(self):
        res = '['
        for i in range(self.__size):
            res += '{}: {}, '.format(i, self.list[i])
        res += ']'
        return res

    def __len__(self):
        return self.__size

    def get_hash(self, key, i):
        return self.__func(key, i)

    def insert(self, key):
        i = 0
        while i <= self.__size:
            hash_key = self.get_hash(key, i)
            print("key = {}, hash_key = {}".format(key, hash_key))
            i += 1
            if self.list[hash_key] == None or self.list[hash_key] == 'deleted':
                self.list[hash_key] = key
                return
        raise Exception("Table is full")

    def search(self, key):
        i = 0
        hash_key = self.get_hash(key, i)
        while i <= self.__size or self.list[hash_key] != None:
            i += 1
            hash_key = self.get_hash(key, i)
            if self.list[hash_key] == key:
                return hash_key
        return None

    def delete(self, key):
        ind = self.search(key)
        if ind == None:
            raise ValueError("No such element in the table")
        self.list[ind] = 'deleted'


ht = HashTable(128)
for i in range(30):
    ht.insert(i * 10)
print(ht)
elem = ht.search(25)
print('elem = {}, 20 = {}'.format(elem, ht.search(20)))
ht.delete(25)
ht.delete(10)
print(ht)
