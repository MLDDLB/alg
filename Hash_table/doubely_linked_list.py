class ListNode:

    def __init__(self, key = -1, data = None, prev = None, next = None):
        self.__key = key
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str("[{}: {}]".format(self.__key, self.data))

    def __hash__(self):
        return hash(self.__key)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

class DLinkedList:

    def __init__(self):
        self.head = ListNode(data = None)
        self.length = 0
        self.head.prev = self.head
        self.head.next = self.head

    def __str__(self):
        x = self.head.next
        res = str(self.head)
        while x != self.head:
            res += " - {}".format(x)
            x = x.next
        return res

    def __len__(self):
        return self.length

    def find(self, key):
        if self.length == 0:
            raise IndexError("list is empty")
        x = self.head
        while x.key != key:
            x = x.next
            if x is self.head:
                return None
        return x

    def insert(self, node_key, pos = None):
        if self.length == 0:
            self.head.key = node_key
            self.length = 1
            return
        if pos == None:
            pos = self.head
        elif type(pos) != ListNode:
            raise TypeError("Position argument must be a ListNode")
        new_node  = ListNode(key = node_key)
        new_node.next = pos
        pos.prev.next = new_node
        new_node.prev = pos.prev
        pos.prev = new_node
        if pos == self.head:
            self.head = new_node
        self.length += 1

    def delete(self, pos = None):
        if self.length == 0:
            raise IndexError("List is empty")
        if pos == None:
            pos = self.head
        pos.next.prev = pos.prev
        pos.prev.next = pos.next
        if pos == self.head:
            self.head = pos.next
        self.length -= 1




'''a = ListNode(key = 1)
print(a)
print("key = {}".format(a.key))
a.key = 3
ll = DLinkedList()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ptr = ll.find(3)
ll.insert(6, ptr)
print(ll)
ll.delete()
ll.delete(ptr)
print(ll)'''
