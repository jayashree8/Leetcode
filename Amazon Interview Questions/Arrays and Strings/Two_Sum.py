'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

nums = [2,7,11,15]
target = 9

''' MY CODE '''
output = []

for i in range(len(nums)):
    if target-nums[i] in nums[i+1:]:
        output.append(i)
        output.append(nums[i+1:].index(target-nums[i])+i+1)
        break
print(output)

''' OPTIMUM CODE '''
dict1 = {}
for i, num in enumerate(nums):
    if target - num in dict1:
        print([i,dict1[target-num]])
    else:
        dict1[num] = i
