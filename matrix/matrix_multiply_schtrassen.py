from matrix import Matrix
from matrix_multiply import SquareMatrixMultiplyRecursuve
import time

def SchtrassenMultiply(mat_1, mat_2):
    if not type(mat_1) == Matrix or not type(mat_2) == Matrix: raise TypeError("Argument must be a matrix")
    elif not mat_1.IsSquareMatrix() or not mat_2.IsSquareMatrix(): raise ValueError("Argument must be a square matrix")
    elif mat_1.Rows != mat_2.Rows: raise ValueError("Both arguments should have equal sizes")
    else:
        size = mat_1.Rows
        if size == 1:
            res = mat_1 * mat_2
            return res
        else:
            q = int(size/2)
            A11 = Matrix([[col for col in row[:q]] for row in mat_1[:q]])
            A12 = Matrix([[col for col in row[q:]] for row in mat_1[:q]])
            A21 = Matrix([[col for col in row[:q]] for row in mat_1[q:]])
            A22 = Matrix([[col for col in row[q:]] for row in mat_1[q:]])
            B11 = Matrix([[col for col in row[:q]] for row in mat_2[:q]])
            B12 = Matrix([[col for col in row[q:]] for row in mat_2[:q]])
            B21 = Matrix([[col for col in row[:q]] for row in mat_2[q:]])
            B22 = Matrix([[col for col in row[q:]] for row in mat_2[q:]])
            P1 = SchtrassenMultiply(A11, B12) - SchtrassenMultiply(A11, B22)
            P2 = SchtrassenMultiply(A11, B22) + SchtrassenMultiply(A12, B22)
            P3 = SchtrassenMultiply(A21, B11) + SchtrassenMultiply(A22, B11)
            P4 = SchtrassenMultiply(A22, B21) - SchtrassenMultiply(A22, B11)
            P5 = SchtrassenMultiply(A11, B11) + SchtrassenMultiply(A11, B22) + SchtrassenMultiply(A22, B11) + SchtrassenMultiply(A22, B22)
            P6 = SchtrassenMultiply(A12, B21) + SchtrassenMultiply(A12, B22) - SchtrassenMultiply(A22, B21) - SchtrassenMultiply(A22, B22)
            P7 = SchtrassenMultiply(A11, B11) + SchtrassenMultiply(A11, B12) - SchtrassenMultiply(A21, B11) - SchtrassenMultiply(A21, B12)
            res11 = P5 + P4 - P2 + P6
            res12 = P1 + P2
            res21 = P3 + P4
            res22 = P5 + P1 - P3 -P7
            (res11.ExtendRight(res12)).ExtendDown(res21.ExtendRight(res22))
            return res11



#mat1 = Matrix([1,2], [3, 4])
#mat2 = Matrix([5, 6], [7, 8])
mat1 = Matrix([1, 2, 3, 4, 10, 10, 5, 2], [5, 6, 7, 8, 1, 1, 7, 3], [9, 10, 11, 12, 9, 8, 3, 5], [13, 14, 15, 16, 1, 4, 9, 5], [1, 2, 3, 4, 10, 10, 5, 2], [13, 14, 15, 16, 1, 4, 9, 5], [9, 10, 11, 12, 9, 8, 3, 5], [5, 6, 7, 8, 1, 1, 7, 3])
mat2 = Matrix([16, 15, 14, 13, 50, 3, 2, 1], [12, 11, 10, 9, 4, 5, 6, 1], [8, 7, 6, 5, 8, 4, 3, 7], [4, 3, 2, 1, 1, 2, 3, 4], [16, 15, 14, 13, 50, 3, 2, 1], [12, 11, 10, 9, 4, 5, 6, 1], [8, 7, 6, 5, 8, 4, 3, 7], [4, 3, 2, 1, 1, 2, 3, 4])
start_time_scht = time.time()
mat3 = SchtrassenMultiply(mat1, mat2)
end_time_scht = time.time()
start_time_simple = time.time()
mat4 = mat1 * mat2
end_time_simple = time.time()
start_time_recur = time.time()
mat5 = SquareMatrixMultiplyRecursuve(mat1, mat2)
end_time_recur = time.time()
print("mat3 = {} \n time = {}".format(mat3, end_time_scht - start_time_scht))
print("mat4 = {} \n time = {}".format(mat4, end_time_simple - start_time_simple))
print("mat5 = {} \n time = {}".format(mat5, end_time_recur - start_time_recur))
