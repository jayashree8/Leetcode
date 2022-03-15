'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
'''
import math
s = "3.14159"

''' MY CODE '''
neg=1
c=""
flag=0
for i in s:
    if i==' ':
        if flag>0:
            break
        continue
    elif i.isalpha():
        flag+=1
        break
    elif i=='+':
        flag+=1
        if flag>=2:
            break
    elif i=='-':
        flag+=1
        if flag>=2:
            break
        neg=-1
    else:
        flag+=1
        c+=i
if c=="":
    print(0)
res=int(float(c))
if -2**(31)>res*neg:
    print(-2**(31))
if 2**(31)-1<res*neg:
    print(2**(31)-1)
print(res*neg)
