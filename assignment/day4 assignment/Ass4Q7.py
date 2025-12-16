# Matrix 1: 3x4 as list of lists
matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Matrix 2: 3x4 as tuple of tuples
matrix_tuple = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

# Function to calculate addition and subtraction
def add_sub_matrices(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])

    add_result = []
    sub_result = []

    for i in range(rows):
        add_row = []
        sub_row = []
        for j in range(cols):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
        add_result.append(add_row)
        sub_result.append(sub_row)

    return add_result, sub_result


# Main
addition, subtraction = add_sub_matrices(matrix_list, matrix_tuple)

print("Addition Result:")
for row in addition:
    print(row)

print("\nSubtraction Result:")
for row in subtraction:
    print(row)
