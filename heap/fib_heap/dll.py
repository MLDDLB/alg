import sys

class DLLNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class DLLIterator:

    def __init__(self, linked_list):
        self._collection = linked_list
        self._stop = len(linked_list)
        self._cursor = 0
        if linked_list.head is not None:
            self._current = linked_list.head.left
        else:
            self._current = None

    def __next__(self):
        if self._cursor >= self._stop or self._current is None:
            raise StopIteration()
        self._cursor += 1
        self._current = self._current.right
        return self._current

class DLL:

    def __init__(self):
        self.head = None
        self.__size = 0
        # self.__current = self.head
        # self.__index = 0

    def __len__(self):
        return self.__size

    def __str__(self):
        if self.head is None:
            return str(None)
        current_node = self.head.right
        res_list = [str(self.head), ]
        while current_node is not self.head:
            res_list.append(str(current_node))
            current_node = current_node.right
        return "->".join(res_list)

    def __iter__(self):
        return DLLIterator(self)

    # def __next__(self):
    #     self.__current = self.__current.right
    #     if self.__index < self.__size:
    #         self.__index += 1
    #         return self.__current
    #     else:
    #         self.__current = self.head
    #         self.__index = 0
    #         raise StopIteration()

    def unite(self, list_1, list_2):
        new_list = DLL()
        if list_1.head is not None and list_2.head is not None:
            buf = list_1.head.left
            list_1.head.left.right = list_2.head
            list_2.head.left.right = list_1.head
            list_1.head.left = list_2.head.left
            list_2.head.left = buf
            new_list.head = list_1.head
            new_list.size = list_1.__size + list_2.__size
        elif list_1.head is None and list_2.head is not None:
            new_list.head = list_2.head
            new_list.__size = list_2.__size
        elif list_1.head is not None:
            new_list.head = list_1.head
            new_list.__size = list_1.__size
        return new_list


    def search(self, key):
        if self.head is None:
            return None
        current_node = self.head
        if current_node.key == key:
            return current_node
        current_node = current_node.right
        while current_node is not self.head and current_node.key != key:
            current_node = current_node.right
        if current_node is self.head:
            return None
        else:
            return current_node

    def swap(self, first_node, second_node):
        buf = first_node.key
        first_node.key = second_node.key
        second_node.key = buf

    def get_last(self):
        current_node = self.head
        if current_node is None:
            return None
        return self.head.left

    def insert(self, val):
        if not isinstance(val, DLLNode):
            new_node = DLLNode(val)
        else:
            new_node = val
        if self.head is None:
            self.head = new_node
            new_node.right = new_node
            new_node.left = new_node
        else:
            new_node.right = self.head
            self.head.left.right = new_node
            new_node.left = self.head.left
            self.head.left = new_node
            self.head = new_node
        self.__size += 1

    def delete(self, node):
        node.right.left = node.left
        node.left.right = node.right
        if node is self.head:
            self.head = node.right
        if self.__size == 1:
            self.head = None
        self.__size -= 1


if __name__ == "__main__":
    linked_list = DLL()
    while inp := sys.stdin.readline().strip():
        linked_list.insert(int(inp))
    print(linked_list)
    while inp := sys.stdin.readline().strip():
        nd = linked_list.search(int(inp))
        linked_list.delete(nd)
        print(linked_list)
    itr = iter(linked_list)
    while True:
        try:
            print(next(itr))
        except StopIteration:
            break
