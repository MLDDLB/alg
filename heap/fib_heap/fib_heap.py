import sys
import math
from dll import DLL, DLLNode, DLLIterator
from collections import deque

class FibHeapNode(DLLNode):

    child = DLL()
    mark = False
    parent = None
    degree = 0

    def __str__(self):
        return str((self.key, self.mark))

    def __repr__(self):
        return str((self.key, self.mark))


class FibHeap:

    def __init__(self):
        self.root_list = DLL()
        self.extr = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        dq = deque()
        dq.append(self.root_list)
        res = ""
        while dq:
            cur_list = dq.popleft()
            res += f"{str(cur_list)}\n"
            for node in cur_list:
                if node.child.head is not None:
                    dq.append(node.child)
        return res

class MinFibHeap(FibHeap):

    def insert(self, node):
        node.degree = 0
        node.parent = None
        node.child = DLL()
        node.mark = False
        self.root_list.insert(node)
        if self.extr is None:
            self.extr = node
        elif node.key < self.extr.key:
            self.extr = node
        self.size += 1

    def consolidate(self):
        max_degree = math.ceil(math.log2(self.size))
        degree_array = [None for i in range(max_degree+1)]
        for node in self.root_list:
            current_node = node
            degree = current_node.degree
            while degree_array[degree] is not None:
                other_node = degree_array[degree]
                if current_node.key > other_node.key:
                    self.root_list.swap(current_node, other_node)
                self.link(other_node, current_node)
                degree_array[degree] = None
                degree += 1
            degree_array[degree] = current_node
        self.extr = None
        for i in range(max_degree+1):
            if degree_array[i] is not None:
                if self.extr is None:
                    self.root_list = DLL()
                    self.root_list.insert(degree_array[i])
                    self.extr = degree_array[i]
                else:
                    self.root_list.insert(degree_array[i])
                    if degree_array[i].key < self.extr.key:
                        self.extr = degree_array[i]

    def link(self, first_node, second_node):
        self.root_list.delete(first_node)
        second_node.child.insert(first_node)
        first_node.parent = second_node
        second_node.degree += 1
        first_node.mark = False

    def extract_min(self):
        min = self.extr
        if min is not None:
            for node in min.child:
                self.insert(node)
                node.parent = None
            self.root_list.delete(min)
            if min == min.right:
                self.extr = None
            else:
                self.extr = min.right
                self.consolidate()
            self.size -= 1
        return min

    @classmethod
    def union(cls, heap1, heap2):
        new_heap = MinFibHeap()
        new_heap.extr = heap1.extr
        last_node = heap1.root_list.get_last()
        if last_node is not None and heap2.root_list.head is not None:
            last_node.right = heap2.root_list.head
            heap2.root_list.head.left.right = heap1.root_list.head
            heap1.root_list.head.left = heap2.root_list.head.left
            heap2.root_list.head.left = last_node
            new_heap.root_list = heap1.root_list
        elif last_node is None and heap2.root_list.head is not None:
            new_heap.root_list = heap2.root_list
        else:
            new_heap.root_list = heap1.root_list
        if heap1.extr is None or heap2.extr is not None and heap2.extr.key < heap1.extr.key:
            new_heap.extr = heap2.extr
        new_heap.size = heap1.size + heap2.size
        return new_heap

    def get_min(self):
        return self.extr

    def decrease_key(self, node, key):
        if key > node.key:
            raise ValueError("New key is greater than previous")
        node.key = key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self.cut(node, parent)
            self.cascading_cut(parent)
        if node.key < self.extr.key:
            self.extr = node

    def cut(self, node, parent):
        parent.child.delete(node)
        parent.degree -= 1
        self.insert(node)
        node.parent = None
        node.mark = False

    def cascading_cut(self, node):
        parent = node.parent
        if parent is not None:
            if node.mark == False:
                node.mark = True
            else:
                self.cut(node, parent)
                self.cascading_cut(parent)


class MaxFibHeap(FibHeap):

    def insert(self, node):
        node.degree = 0
        node.parent = None
        node.child = DLL()
        node.mark = False
        self.root_list.insert(node)
        if self.extr is None:
            self.extr = node
        elif node.key < self.extr.key:
            self.extr = node
        self.size += 1

    def get_max(self):
        return self.extr



fb = MinFibHeap()
while inp := sys.stdin.readline().strip():
    fb.insert(FibHeapNode(int(inp)))
print(fb.root_list)
min = fb.extract_min()
print(fb.root_list, min)
for node in fb.root_list:
    print(node, node.degree)
for node in fb.root_list:
    print(node, node.degree)
print(fb.extr.child)
print(fb)
