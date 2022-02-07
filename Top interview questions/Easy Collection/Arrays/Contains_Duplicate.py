''' 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true
'''

''' MY CODE '''
nums = [3,1]

if sorted(list(set(nums))) == sorted(nums):
    print('False')
else:
    print('True')