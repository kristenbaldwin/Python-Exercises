matrix_list1 = [ [2, -2],
                [5, 3] ]
matrix_list2 = [ [1, 4],
                [-3, 2] ]
matrix_sum = [ [0, 0],
                [0, 0] ]

for r in range(len(matrix_list1):
    for c in range(len(matrix_list1[0]):
        matrix_sum[r][c] = ((matrix_list1[r][c] * matrix_list2[r][c]) + (matrix_list1[r][c + 1] * matrix_list2[r + 1][c]))
for x in matrix_sum:
    print(x)