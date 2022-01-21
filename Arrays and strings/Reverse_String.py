'''
Write a function that reverses a string. The input string is given as an array of characters s.
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''

''' MY CODE '''
s = ["h","e","l","l","o"]
temp = "".join(s)[::-1]
print(list(temp))