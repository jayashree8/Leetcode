'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Input: nums = [1,1,0,1,1,1]
Output: 3
'''

''' MY CODE '''
import re

nums = [1,1,0,1,1,1]

lst = [str(i) for i in nums]
temp = "".join(lst)

output = re.findall("1+",temp)
max = 0
for i in output:
    if len(i)>max:
        max = len(i)

print(max)
