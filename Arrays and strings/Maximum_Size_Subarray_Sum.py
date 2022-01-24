'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''

''' MY CODE '''
target = 7
nums = [2,3,1,2,4,3]

left = 0
sum = 0
count = len(nums)

for right in range(len(nums)):
    sum = sum + nums[right]

    if sum<target:
        continue

    while(sum>=target and left<=right):
        sum = sum - nums[left]
        left = left+1

    count = min(count,right-left+2)

if left==0 and sum<target:
    print(0)
else:
    print(count)
    