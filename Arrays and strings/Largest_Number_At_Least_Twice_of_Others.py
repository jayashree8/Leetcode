'''
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
'''

''' MY CODE
nums = [3,6,1,0]

def dominantIndex(nums):
    max_val = max(nums)
    max_index = nums.index(max_val)

    if len(nums) == 1:
        return 0
    else:
        nums.pop(max_index)
        #print(nums)
        list2 = [x*2 for x in nums]
        #print(list2)
        for i in list2:
            if max_val<i:
                return -1
                #break
        return max_index

print(dominantIndex(nums))
'''

''' OPTIMIZED CODE'''
def dominantIndex(nums):
    if len(nums) <= 1:
        return 0
        
    sorted_nums = sorted(nums)
    max_num = sorted_nums[-1]
    second_max = sorted_nums[-2]
        
    if max_num >= second_max * 2:
        return nums.index(max_num)
        
    return -1