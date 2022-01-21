'''
Given two binary strings a and b, return their sum as a binary string.
Input: a = "11", b = "1"
Output: "100"
'''

''' MY CODE'''
a = '11'
b= '1'

output = bin(int(a,2)+int(b,2))
print(output[2:])