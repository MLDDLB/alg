from collections import deque

class Node:
    """
    Use as elements of the 'Heap' class to store data, keys and links to other elements.

    Main use: As an element of the Heap or the binary tree

    Attributes
    ----------
    key: int
        Element key
    right: Node
        Right successor of the element
    left: Node
        Left successor of the element
    parent: Node
        Predecessor of the element

    Methods
    -------
    copy():
        Create a copy of the Node and return it
    """

    def __init__(self, value):
        """
        Inits Node.

        Arguments
        ---------
        key: int
            Element key
        right: Node
            Right successor of the element
        left: Node
            Left successor of the element
        parent: Node
            Predecessor of the element
        """

        self.key = value
        self.right = None
        self.left = None
        self.parent = None

    def __str__(self):
        """Return a string of the key of the node"""
        return str(self.key)

    def copy(self):
        """Create a copy of the Node and return it"""
        newNode = Node(self.key)
        newNode.parent = self.parent
        newNode.left = self.left
        newNode.right = self.right
        return newNode


class Heap:
    """
    A class used to recreate a heap data structure

    This class is used as subclass of the 'MinHeap' and 'MaxHeap' classes and
    has no uses in intself.

    Attributes
    ----------
    heap_size: int
        number of elements of the heap
    head: Node
        pointer to the head node of the heap
    null: Node
        pointer to the null limiter node of the heap
    """

    def __init__(self):
        """
        Inits 'Heap'

        The constructor does not accept any arguments and just creates a heap
        structure. Head node is None, null node inits as a 'Node' with None value
        and 'heap_size' inits as 0
        """
        self.heap_size = 0
        self.head = None
        self.null = Node(None)
        self.null.right = self.head
        self.null.left = self.head

    def __getitem__(self, key):
        """
        Get the element with the corresponding key from the heap

        Argumnets
        ---------
        key: int
            key of the element you're trying to get
        """
        x = self.head
        nodeStack = deque()
        while key != x.key:
            if x.right is not None:
                nodeStack.append(x.right)
            if x.left is not None:
                nodeStack.append(x.left)
            if not bool(nodeStack):
                x = None
                break
            x = nodeStack.pop()
        return x

    def __len__(self):
        """Return the size of the heap"""
        return self.headpSize

    def __str__(self):
        """
        Return a string containing all elements of the heap.

        Walk the heap horizontally and add elements to the string
        level-by-level. Separate the elements with spaces.
        """
        res = ""
        nodeStack = deque()
        nodeStack.append(self.head)
        while bool(nodeStack):
            x = nodeStack.popleft()
            print("pop = {}".format(x))
            res += "{} ".format(x)
            print("res = {}".format(res))
            if x.left is not self.null:
                nodeStack.append(x.left)
            if x.right is not self.null:
                nodeStack.append(x.right)
        return res

class MinHeap(Heap):
    """
    Extend 'Heap'.

    All heap elements are in a non-increasing order

    Attributes
    ----------
    heap_size: int
        number of elements of the heap
    head: Node
        pointer to the head node of the heap
    null: Node
        pointer to the null limiter node of the heap

    Methods
    -------
    MinHeapify(x):
        Perserve the min heap property and return a pointer to the element.
    DecreaseKey(x, key):
        Decrease the key of the element and move it to the right place.
    Swap(x, y):
        Swap two Nodes of the Heap.
    Insert(key):
        Insert a new element into the heap.
    GetMin():
        Return the head of the heap, which is the minimum element.
    ExtractMin():
        Retrun the head of the heap and delete it.
    Union(otherHeap):
        Unify two heaps into one.
    """

    def __init__(self):
        """
        Inits MinHeap

        The constructor does not accept any arguments and just creates a heap
        structure. Head node is None, null node inits as a 'Node' with None value
        and 'heap_size' inits as 0.
        """
        self.heap_size = 0
        self.head = None
        self.null = Node(None)
        self.null.right = self.head
        self.null.left = self.head


    def Swap(self, x, y):
        """Swap two Nodes of the Heap.

        Interchange keys and data of two elements, but leave successor and
        predecessor attributes the same.

        Keyword arguments:
        x --- Node that will replace x node
        y --- Node that will replace y node

        Raises
        ------
        TypeError:
            If at least one of the arguments is not Node raise TypeError
        ValueError:
            If at least one of the Nodes is a None-node raise ValueError
        """
        if type(x) != Node or type(y) != Node:
            raise TypeError("Both arguments must be nodes")
        if x.key == None or y.key == None:
            raise ValueError("Can't swap with a None-node")
        buf = x.key
        x.key = y.key
        y.key = buf


    def MinHeapify(self, x):
        """Perserve the min heap property and return a pointer to the element.

        Since only the keys of the elements change, and elements themselves stay
        the same, return a pointer to the element that has the key of the
        starting element at the end of the method.

        Argumnets
        ---------
        x: Node of the heap that will be moved to the right place in the
              heap
        """
        while True:
            if x.left is not self.null and x.left.key < x.key:
                smallest = x.left
            else:
                smallest = x
            if x.right is not self.null and x.right.key < smallest.key:
                smallest = x.right
            if smallest != x:
                self.Swap(x, smallest)
                x = smallest
            else:
                break
        return smallest
                #self.MinHeapify(smallest)

    def Decreasekey(self, x, key):
        """
        Decrease the key of the element and move it to the right place in the heap

        Arguments
        ---------
        x: Node
            node whose key will be decreased
        key: int
            a number to wich the element key will be decreased

        Raises
        ------
        ValueError:
            If the new key is greater than the old raise ValuerError
        """
        if key > x.key:
            raise ValueError("The current value is lesser than the new one")
        x.key = key
        while x is not self.head and x.key < x.parent.key:
            self.Swap(x, x.parent)
            x = x.parent

    def Insert(self, key):
        """
        Insert a new element into the heap.

        Create a node, and if the heap is empty, place it in it's head. If the
        heap is not empty, find the end of the heap and place the element there.
        Then move it to the right place in the heap to perserve the min heap
        property.

        Argumnets
        ---------
        key: int
            a number representing the key of the new element
        """
        newNode = Node(float("inf"))
        if self.head is None:
            self.head = newNode
            self.Decreasekey(newNode, key)
            self.head.right = self.head.left = self.null
            self.head.parent = self.null
            self.heap_size += 1
            pass
        nodeStack = deque()
        nodeStack.append(self.head)
        while True:
            x = nodeStack.popleft()
            if x.left is self.null:
                x.left = newNode
                newNode.parent = x
                newNode.left = self.null
                newNode.right = self.null
                break
            elif x.right is self.null:
                x.right = newNode
                newNode.parent = x
                newNode.left = self.null
                newNode.right = self.null
                break
            else:
                nodeStack.append(x.left)
                nodeStack.append(x.right)
        self.heap_size += 1
        self.Decreasekey(newNode, key)

    def Delete(self, x):
        """
        Delete the element from the heap.

        Assign an 'inf' key to the element and then move it to the end of the
        heap in order to perserve the min heap property. After that, delete it.

        Arguments
        ---------
        x:
            the node that will be deleted from the heap.

        Raises
        ------
        IndexError:
            if there are no elements left in the heap raise IndexError
        ValueError:
            if the key of the element to delete is 'None' raise ValueError
        """
        if self.head is None:
            raise IndexError("Heap is empty")
        elif x.key is None:
            raise ValueError("Can't delete the null element")
        else:
            x.key = float('inf')
            x = self.MinHeapify(x)
            if x is x.parent.right:
                x.parent.right = self.null
            else:
                x.parent.left = self.null

    def GetMin(self):
        """Return the head of the heap, which is the minimum element."""
        if self.head is not None:
            return self.head
        else:
            print("Heap is empty")

    def ExtractMin(self):
        """
        Retrun the head of the heap and delete it.

        Save the minimum element, which is the head of the heap in the 'minimum'
        variable. Then call the 'Delete' method to perserve the min property of
        the heap and delete the head.

        Raises
        ------
        IndexError:
            if there are no elements in the heap raise IndexError
        """
        if self.head is None:
            raise IndexError("Heap is empty")
        minimum = self.head.key
        self.Delete(self.head)
        return minimum

    def Union(self, otherHeap):
        """
        Unify two heaps into one.

        Walk the second heap horizontally and add the elements to the queue.
        Then call the method 'Insert' to add the elements of the second heap
        to the first one-by-one.

        Arguments
        ---------
        otherHeap: Heap
            the heap whose elements will be added to the first heap

        Raises
        ------
        TypeError:
            if the argument is not heap raise TypeError
        """
        if type(otherHeap) != MinHeap:
            raise TypeError("Argument must be a heap")
        nodeQueue = deque()
        nodeQueue.append(otherHeap.head)
        while nodeQueue:
            x = nodeQueue.popleft()
            if x.left is not otherHeap.null:
                print("left = {}".format(x.left))
                nodeQueue.append(x.left)
            if x.right is not otherHeap.null:
                print("right = {}".format(x.right))
                nodeQueue.append(x.right)
            self.Insert(x.key)


def main():
    myHeap = MinHeap()
    while True:
        try:
            myHeap.Insert(int(input("Enter a number: ")))
        except KeyboardInterrupt:
            break
    print("myHeap = {}".format(myHeap))
    myHeap.Delete(myHeap[5])
    print("myHeap = {}".format(myHeap))
    print("min = {}".format(myHeap.ExtractMin()))
    print("myHeap = {}, head = {}, left = {}, right = {}".format(myHeap, myHeap.head, myHeap.head.left, myHeap.head.right))
    secondHeap = MinHeap()
    while True:
        try:
            secondHeap.Insert(int(input("Enter a number: ")))
        except KeyboardInterrupt:
            break
    print("secondHeap = {}".format(secondHeap))
    myHeap.Union(secondHeap)
    print("myHeap = {}".format(myHeap))
    print("Node doc = {}".format(Node.__doc__))
    print("Unify doc = {}".format(MinHeap.Union.__doc__))

if __name__ == "__main__":
    main()
