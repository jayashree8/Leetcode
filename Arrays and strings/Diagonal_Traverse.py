'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
'''

''' MY CODE'''
import collections

mat = [[1,2,3],[4,5,6],[7,8,9]]

d = collections.defaultdict(list)

for i in range(len(mat)):
    for j in range(len(mat[i])):
        d[i+j].append(mat[i][j])

output = []

for i in d.items():
    if i[0]%2==0:
        output.extend(i[1][::-1])
    else:
        output.extend(i[1])

print(output)