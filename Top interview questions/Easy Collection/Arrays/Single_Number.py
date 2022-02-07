'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1
'''

''' MY CODE '''
nums = [2,2,1]

dict1 = {}

for i in nums:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] += 1

for key,value in dict1.items():
    if value==1:
        print(key)

''' OPTIMUM CODE '''
#Xor operator is used for finding unique value as a^a=0
output = 0
for i in nums:
    output ^= i
print(output)
