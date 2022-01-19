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