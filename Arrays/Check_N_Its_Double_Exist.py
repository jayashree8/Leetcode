'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
'''

''' MY CODE '''
arr = [-2,0,10,-19,4,6,-8]

mp = set()
flag = 0

for elem in arr:
    if (elem*2) in mp or (elem*0.5) in mp:
        flag = 1
    mp.add(elem)

if flag==1:
    print('True')
else:
    print('False')