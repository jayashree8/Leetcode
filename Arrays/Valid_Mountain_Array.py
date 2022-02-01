'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Input: arr = [0,3,2,1]
Output: true

There are some conditons as well to form a mountain:

The array size has to be > 3
It has to be strictly increasing like [0, 3, 5] and the values has to be different not same
Similarly it has to be strictly decreasing like [4 , 2, 1] amd the values has to be different not same
So, how we can check it. For that one we will use the help of 2 pointers one will start from left & another will start from right. 
If left and right meets on same index value then we return true, because it's a stricly increasing and decreasing mountain.
'''

''' MY CODE '''
arr = [0, 2, 3, 3, 4, 5, 2, 1, 0]
flag = 0

if len(arr) < 3: 
    flag =1
else:
    l = 0
    r = len(arr) - 1
    while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]: 
        l += 1
    while r - 1 > 0 and arr[r] < arr[r - 1]: 
        r -= 1
    if l!=r:
        flag = 1

if flag==1:
    print('False')
else:
    print('True')
        
