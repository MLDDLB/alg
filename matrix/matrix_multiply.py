from matrix import Matrix
import time

def SquareMatrixMultiplyRecursuve(mat_1, mat_2):
    #print("mat_1 = {} \n mat_2 = {} ".format(mat_1, mat_2))
    if not type(mat_1) == Matrix or not type(mat_2) == Matrix: raise TypeError("Argument must be a matrix")
    elif not mat_1.IsSquareMatrix() or not mat_2.IsSquareMatrix(): raise ValueError("Argument must be a square matrix")
    elif mat_1.Rows != mat_2.Rows: raise ValueError("Both arguments should have equal sizes")
    else:
        #print("mat_1 = {} \n mat_2 = {} ".format(mat_1, mat_2))
        size = mat_1.Rows
        #print("size = {}".format(size))
        #res = Matrix(size, size)
        #print("res = {}".format(res))
        if size == 1 :
            res = mat_1 * mat_2
            #print("res = {} * {} = {}".format(mat_1, mat_2, res))
            return res
        else:
            q = int(size/2)
            A11 = Matrix([[col for col in row[0:q]] for row in mat_1[0:q]])
            #print("A11 = {}".format(A11))
            A12 = Matrix([[col for col in row[q:]] for row in mat_1[:q]])
            #print("A12 = {}".format(A12))
            A21 = Matrix([[col for col in row[:q]] for row in mat_1[q:]])
            #print("A21 = {}".format(A21))
            A22 = Matrix([[col for col in row[q:]] for row in mat_1[q:]])
            #print("A22 = {}".format(A22))
            B11 = Matrix([[col for col in row[0:q]] for row in mat_2[0:q]])
            #print("B11 = {}".format(B11))
            B12 = Matrix([[col for col in row[q:]] for row in mat_2[:q]])
            #print("B12 = {}".format(B12))
            B21 = Matrix([[col for col in row[:q]] for row in mat_2[q:]])
            #print("B21 = {}".format(B21))
            B22 = Matrix([[col for col in row[q:]] for row in mat_2[q:]])
            #print("B22 = {}".format(B22))
            res11 = SquareMatrixMultiplyRecursuve(A11, B11) + SquareMatrixMultiplyRecursuve(A12, B21)
            #print("res11 = {}".format(res11))
            res12 = SquareMatrixMultiplyRecursuve(A11, B12) + SquareMatrixMultiplyRecursuve(A12, B22)
            #print("res12 = {}".format(res12))
            res21 = SquareMatrixMultiplyRecursuve(A21, B11) + SquareMatrixMultiplyRecursuve(A22, B21)
            #print("res21 = {}".format(res21))
            res22 = SquareMatrixMultiplyRecursuve(A21, B12) + SquareMatrixMultiplyRecursuve(A22, B22)
            #print("res22 = {}".format(res22))
            (res11.ExtendRight(res12)).ExtendDown(res21.ExtendRight(res22))
            #print("res11 = {}".format(res11))
            return res11

'''mat1 = Matrix([1, 2, 3, 4, 10, 10, 5, 2], [5, 6, 7, 8, 1, 1, 7, 3], [9, 10, 11, 12, 9, 8, 3, 5], [13, 14, 15, 16, 1, 4, 9, 5], [1, 2, 3, 4, 10, 10, 5, 2], [13, 14, 15, 16, 1, 4, 9, 5], [9, 10, 11, 12, 9, 8, 3, 5], [5, 6, 7, 8, 1, 1, 7, 3])
mat2 = Matrix([16, 15, 14, 13, 50, 3, 2, 1], [12, 11, 10, 9, 4, 5, 6, 1], [8, 7, 6, 5, 8, 4, 3, 7], [4, 3, 2, 1, 1, 2, 3, 4], [16, 15, 14, 13, 50, 3, 2, 1], [12, 11, 10, 9, 4, 5, 6, 1], [8, 7, 6, 5, 8, 4, 3, 7], [4, 3, 2, 1, 1, 2, 3, 4])
start_time_recur = time.time()
mat3 = SquareMatrixMultiplyRecursuve(mat1, mat2)
end_time_recur = time.time()
start_time_simple = time.time()
mat4 = mat1 * mat2
end_time_simple = time.time()
print("mat3 = {} \n time = {}".format(mat3, end_time_recur - start_time_recur))
print("mat4 = {} \n time = {}".format(mat4, end_time_simple - start_time_simple))'''
