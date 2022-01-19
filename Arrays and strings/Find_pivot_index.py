'''
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
'''

''' MY CODE
# Initializing a list and pivot
nums = [1,7,3,6,5,6]
pivot = 0

# Length of the list
l = len(nums)

# Conditions
for i in range (0,l):
    print(i)
    print(sum(nums[0:i]))
    print(sum(nums[i+1:l]))
    print('---------------')

    if i==0:
        if sum(nums[1:l]) == 0:
            pivot = 0
            break
    elif i==l-1:
        if sum(nums[0:l-1]) == 0:
            pivot = l-1
            break
    elif sum(nums[0:i]) == sum(nums[i+1:l]):
        pivot = i 
        break
    else:
        pivot = -1

print(pivot)
'''

''' OPTIMUM CODE'''
# Initializing a list, pivot and leftsum
nums = [1,7,3,6,5,6]
pivot = 0
leftsum = 0

# Finding sum of the list
s = sum(nums)

# Iterating through the list
for index, val in enumerate(nums):
    if leftsum == s-leftsum-val:
        pivot = index
    leftsum = leftsum + val

print(pivot)
