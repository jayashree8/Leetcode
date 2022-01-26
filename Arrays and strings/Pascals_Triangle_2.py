'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
Input: rowIndex = 3
Output: [1,3,3,1]

In mathematics, Pascal's triangle is a triangular array of the binomial coefficients.
The entry in the nth row and rth column of Pascal's triangle is denoted by nCr
'''

''' MY CODE '''
import math
rowIndex = 3

print([math.comb(rowIndex, i) for i in range(rowIndex + 1)])