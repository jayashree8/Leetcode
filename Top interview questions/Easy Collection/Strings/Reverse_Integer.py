''' 
Given a signed 32-bit integer x, return x with its digits reversed. 

If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Input: x = 123
Output: 321
'''

x = -123

s = str(x)
res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1])
if -2147483648 <= res <= 2147483647:
    print(res)
else:
    print(0)

