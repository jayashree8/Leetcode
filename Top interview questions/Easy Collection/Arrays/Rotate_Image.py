''''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''

''' MY CODE '''
matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(matrix)

matrix = [i[::-1] for i in matrix]
print(matrix)