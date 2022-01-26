'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

nums = [0,1,0,3,12]

count = 0
for i in nums:
    if i==0:
        count = count+1
print(count)

for i in range(count):
    nums.remove(0)
    nums.append(0)
print(nums)