'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

nums = [-1,0,1,2,-1,-4]
output = []

if len(nums)>=3:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum = 0
            temp = []
            sum = nums[i]+nums[j]
            val = -(sum)
            if val in nums and val!=nums[i] and val!=nums[j]:
                temp.extend([nums[i], nums[j], val])
                output.append(temp)
print(output)

ans = []
for i in output:
    a = sorted(i)
    if a not in ans:
        ans.append(a)

print(ans)