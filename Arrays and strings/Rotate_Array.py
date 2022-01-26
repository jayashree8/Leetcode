'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

''' MY CODE '''
nums = [1,2,3,4,5,6,7]
k = 3

lst1 = nums[-k:]
print(lst1)
lst2 = nums[:k+1]
print(lst2)
lst1.extend(lst2)
print(lst1)

''' OPTIMUM CODE '''
while k>0:
    nums.insert(0,nums.pop())
    k = k-1
print(nums)