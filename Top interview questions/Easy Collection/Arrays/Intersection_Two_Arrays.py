''' 
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''

''' MY CODE '''
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

temp = []
for i in nums1:
    if i in nums2:
        nums2.remove(i)
        temp.append(i)

print(temp)