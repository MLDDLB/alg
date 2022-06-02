

class Matrix:

    def __init__(self, *args,rows = 0, columns = 0):
        #print("args = {}; columns = {}; rows = {}".format(args, columns, rows))
        self.List = list()
        self.Columns = columns
        self.Rows = len(args) if len(args) > rows else rows
        col_count = 0
        for arg in args:
            try:
                col_count = len(arg)
                if type(arg[0]) == list:
                    self.List = arg
                    self.Rows = len(arg)
                    self.Columns = len(self.List[0])
                    break
                self.List.append(arg)
            except:
                col_count = 1
                self.List.append([arg])
            if col_count > self.Columns:
                self.Columns = col_count
        n1 = len(self.List)
        #print("n1 = {}".format(n1))
        #print("list = {}; columns = {}; rows = {}".format(self.List, self.Columns, self.Rows))
        for i in range(0, self.Rows):
            if i >= n1:
                self.List.append(list())
            n2 = len(self.List[i])
            #print("i = {}; n2 = {}; list[{}] = {}".format(i, n2, i, self.List[i]))
            for j in range(n2, self.Columns):
                self.List[i].append(0)

    def __getitem__(self, key1, key2 = None):
        if key2 is None:
            return self.List[key1]
        else:
            return self.List[key1][key2]

    def __setitem__(self, key1, value, key2 = None):
        if key2 is None: #and args is not None:
            self.List[key1] = list(value)
        else:
            self[key1][key2] = value

    def __str__(self):
        str = ""
        for i in range(0, self.Rows):
            for j in range(0, self.Columns):
                str = str + ("{} ".format(self.List[i][j]))
            if i == self.Rows - 1:
                break
            str = str + '\n'
        return str

    def __add__(self, other):
        if self.Rows != other.Rows or self.Columns != other.Columns:
            raise ValueError("Sizes don't match")
        else:
            res = Matrix(rows = self.Rows, columns = self.Columns)
            for i in range(0, self.Rows):
                for j in range(0, self.Columns):
                    res.List[i][j] = self.List[i][j] + other.List[i][j]
        return res

    def __sub__(self, other):
        if self.Rows != other.Rows or self.Columns != other.Columns:
            raise ValueError("Sizes don't match")
        else:
            res = Matrix(rows = self.Rows, columns = self.Columns)
            for i in range(0, self.Rows):
                for j in range(0, self.Columns):
                    res.List[i][j] = self.List[i][j] - other.List[i][j]
        return res

    def __mul__(self, other):
        if self.Columns != other.Rows:
            raise ValueError("Sizes don't match")
        else:
            res = Matrix(rows = self.Rows, columns = other.Columns)
            for i in range(0, self.Rows):
                for j in range(0, self.Columns):
                    for k in range(0, self.Columns):
                        res[i][j] = res[i][j] + (self[i][k] * other[k][j])
        return res

    def ExtendRight(self, other):
        if self.Columns != other.Rows:
            raise ValueError("The number of rows must be equal")
        else:
            for i in range(0, other.Rows):
                #print("self[{}] = {}, other[{}] = {}".format(i, self.List[i], i, other.List[i]))
                self.List[i].extend(other.List[i])
                #print("self[{}] = {}".format(i, self.List[i]))
            self.Columns += other.Columns
            return self

    def ExtendDown(self, other):
        if self.Columns != other.Columns:
            raise ValueError("The number of rows must be equal")
        else:
            for i in range(0, other.Rows):
                #print("self[{}] = {}, other[{}] = {}".format(i, self.List[i], i, other.List[i]))
                self.List.append(other.List[i])
                #print("self[{}] = {}".format(i, self.List[i]))
            self.Rows += other.Rows
            return self
    def IsSquareMatrix(self):
        if self.Rows != self.Columns:
            return False
        return True

'''a = Matrix([1, 2, 3, 4],[3,4], 2, 3, 4, 5, 6)
print(a)
print(type(a))
b = (a[0:2])[0:2]
print(b)
print(type(b))
d = Matrix([[col for col in row[0:2]] for row in a[0:2]])
print(d)
f = list([[col for col in row[0:2]] for row in a[0:2]])
print(f)
mat_1 = Matrix([1, 1], [1, 1])
mat_2 = Matrix([2, 2], [2, 2])
mat_1.extend(mat_2)
print(mat_1)'''
