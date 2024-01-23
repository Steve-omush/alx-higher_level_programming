#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
noneL = None
empty_list = []
empty_lists = [[], [], []]
not_list = [42, [2, 5], [1, 2, 3]]
not_all_num = [["blue", 1, 2], [3, 4, "f"], ["23b", 5, 6]]
diff_len = [[1,3,3,3], [3,5,1,2,5], [2,5,8]]
print("the correct matrix.")
print(matrix_divided(matrix, 3))
print(matrix)
try:

    print("1. Passing None as Matrix is None")
    print(matrix_divided(noneL, 3))
    print(noneL)
except Exception as e:
    print(e)
try:

    print("2. the matrix is empty with no Rows")
    print(matrix_divided(empty_list, 2))
    print(empty_list)
except Exception as e:
    print(e)
try:

    print("3. the matrix is empty with rows that are empty.")
    print(matrix_divided(empty_lists, 2))
    print(empty_lists)
except Exception as e:
    print(e)
try:
    print("4. one element is not a list")
    print(matrix_divided(not_list, 3))
    print(not_list)
except Exception as e:
    print(e)
try:
    print("5. Not all are numbers.")
    print(matrix_divided(not_all_num, 3))
    print(not_all_num)
except Exception as e:
    print(e)
try:
    print("6. the rows in matrix are of a different lengths.")
    print(matrix_divided(diff_len, 3))
    print(diff_len)
except Exception as e:
    print(e)
try:
    print("7. the div is 0")
    print(matrix_divided(matrix, 0))
    print(matrix)
except Exception as e:
    print(e)
