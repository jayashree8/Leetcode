'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''

''' MY CODE '''
matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = []

rows = len(matrix)
cols = len(matrix[0])
direction = 1

i = 0
j = -1

while rows*cols>0:
    # Move horizontally
    for _ in range (cols):
        j = j + direction
        output.append(matrix[i][j])
    rows = rows - 1

    # Move vertically
    for _ in range(rows):
        i = i + direction
        output.append(matrix[i][j])
    cols = cols - 1

    direction = direction * -1

print(output)