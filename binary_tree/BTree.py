import sys
from collections import deque

class BTreeNode:

    def __init__(self):
        self.parent = None
        self.size = 0
        self.keys = []
        self.children = []
        self.leaf = False

    def __str__(self):
        return str(self.keys)

    def __repr__(self):
        return str(self.keys)

class BTree:

    def __init__(self, degree):
        self.root = BTreeNode()
        self.root.leaf = True
        self.size = 0
        self.degree = degree

    def __str__(self):
        dq = deque()
        res = str(self.root)
        dq.append(self.root)
        while dq:
            x = dq.popleft()
            for child in x.children:
                res += str(child)
                dq.append(child)
        return res

    def search(self, node, key):
        i = 0
        while i < node.size and key > node.keys[i]:
            i += 1
        if i < node.size and key == node.keys[i]:
            return (node, i)
        elif node.leaf:
            return (None, None)
        else:
            return self.search(node.children[i], key)

    def get_parent(self, node):
        y = None
        x = self.root
        while x is not node:
            y = x
            i = 0
            while i < x.size and node.keys[0] > x.keys[i]:
                i += 1
            x = x.children[i]
        return y

    def succesor(self, node, key):
        i = 0
        while i < node.size and key > node.keys[i]:
            i += 1
        if node.leaf:
            if i < node.size - 1:
                return (node, node.keys[i+1])
            else:
                parent = self.get_parent(node)
                if parent is None:
                    return (None, None)
                i = 0
                while i < parent.size and key > parent.keys[i]:
                    i += 1
                if i < parent.size:
                    return (parent, parent.keys[i])
                else:
                    return (None, None)
        else:
            return (node.children[i+1], node.children[i+1].keys[0])

    def predecessor(self, node, key):
        i = 0
        while i < node.size and key > node.keys[i]:
            i += 1
        if node.leaf:
            if i > 0:
                return (node, node.keys[i-1])
            else:
                parent = self.get_parent(node)
                i = 0
                while i < parent.size and key > parent.keys[i]:
                    i += 1
                if i == 0:
                    return (None, None)
                else:
                    return (parent, parent.keys[i-1])
        else:
            return (node.children[i], node.children[i].keys[-1])

    def merge(self, first_node, second_node):
        for i in range(second_node.size):
            first_node.keys.append(second_node.keys[i])
        if not second_node.leaf:
            for i in range(second_node.size + 1):
                first_node.children.append(second_node.children[i])
        first_node.size += second_node.size
        print(first_node)
        del(second_node)

    def split_child(self, node, i):
        z = BTreeNode()
        y = node.children[i]
        z.size = self.degree - 1
        z.leaf = y.leaf
        z.keys = [0]*(self.degree - 1)
        for j in range(y.size-1, self.degree-1, -1):
            z.keys[j-self.degree] = y.keys[j]
            del[y.keys[j]]
        if not y.leaf:
            for j in range(y.size, self.degree-1, -1):
                z.children.append(y.children[j])
                del(y.children[j])
        y.size = self.degree - 1
        node.children.append(None)
        for j in range(node.size, i, -1):
            node.children[j+1] = node.children[j]
        node.children[i+1] = z
        node.keys.append(0)
        for j in range(node.size, i, -1):
            node.keys[j+1] = node.keys[j]
        node.keys[i] = y.keys[self.degree-1]
        del(y.keys[self.degree-1])
        node.size += 1

    def insert_non_full(self, node, key):
        if node.leaf:
            i = node.size - 1
            node.keys.append(key)
            while i >= 0 and node.keys[i] > key:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = key
            node.size += 1
        else:
            i = node.size - 1
            while i >= 0 and node.keys[i] > key:
                i -= 1
            i += 1
            if node.children[i].size == 2*self.degree - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i = i+1
            self.insert_non_full(node.children[i], key)

    def insert(self, key):
        r = self.root
        if r.size == 2*self.degree - 1:
            s = BTreeNode()
            self.root = s
            s.leaf = False
            s.size = 0
            s.children.append(r)
            r.parent = s
            self.split_child(s, 0)
            self.insert_non_full(s, key)
        else:
            self.insert_non_full(r, key)

    def delete(self, node, key):
        i = 0
        while i < node.size and key > node.keys[i]:
            i += 1

        if i < node.size and key == node.keys[i]:

            if node.leaf:
                del(node.keys[i])
                node.size -= 1
            else:
                (pred, pred_val) = self.predecessor(node, key)

                if pred.size >= self.degree:
                    node.keys[i] = pred_val
                    self.delete(pred, pred_val)
                else:
                    (suc, suc_val) = self.succesor(node, key)
                    if suc.size >= self.degree:
                        node.keys[i] = suc_val
                        self.delete(suc, suc_val)
                    else:
                        pred.keys.append(key)
                        pred.size += 1
                        node.size -= 1
                        self.merge(pred, suc)
                        del(node.keys[i])
                        del(node.children[i+1])
                        if node.size == 0:
                            if node.children:
                                self.root = node.children[0]
                                del(node)

        else:
            if node.children[i].size < self.degree:
                if i-1 >= 0 and node.children[i-1].size >= self.degree:
                    node.children[i].keys.insert(0, node.keys[i-1])
                    node.children[i].size += 1
                    node.keys[i] = node.children[i-1].keys[-1]
                    del(node.children[i-1].keys[-1])
                    node.children[i-1].size -= 1
                    self.delete(node.children[i], key)

                elif i+1 <= node.size and node.children[i+1].size >= self.degree:
                    node.children[i].keys.append(node.keys[i])
                    node.children[i].size += 1
                    node.keys[i] = node.children[i+1].keys[0]
                    del(node.children[i+1].keys[0])
                    node.children[i+1].size -= 1
                    self.delete(node.children[i], key)

                elif i+1 <= node.size:
                    node.children[i].keys.append(node.keys[i])
                    node.children[i].size += 1
                    node.size -= 1
                    del(node.keys[i])
                    del(node.children[i+1])
                    self.merge(node.children[i], node.children[i+1])
                    self.delete(node.chilren[i], key)

                else:
                    node.children[i-1].keys.append(node.keys[i-1])
                    node.children[i-1].size += 1
                    node.size -= 1
                    del(node.keys[i-1])
                    del(node.children[i])
                    self.merge(node.children[i-1], node.children[i])
                    self.delete(node.children[i-1], key)
                    if node.size == 0:
                        if node.children:
                            self.root = node.children[0]
                            del(node)
            else:
                self.delete(node.children[i], key)


tree = BTree(3)
while inp := sys.stdin.readline().strip():
    tree.insert(inp)
print(tree)
(node, i) = tree.search(tree.root, input())
print(tree.succesor(node, node.keys[i]))
print(tree.predecessor(node, node.keys[i]))
tree.delete(tree.root, input())
tree.delete(tree.root, input())
print(tree)
