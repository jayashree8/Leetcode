'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''

''' MY CODE'''
numRows = 5

output = [[None for i in range(j)] for j in range(1, numRows+1)]

for i in range(numRows):
    output[i][0] = 1
    output[i][i] = 1

# Addition of the upper left element and upper right element in the triangle will give the next element
for i in range(2, numRows):
    for j in range(1,i):
        output[i][j] = output[i-1][j-1] + output[i-1][j]

print(output)