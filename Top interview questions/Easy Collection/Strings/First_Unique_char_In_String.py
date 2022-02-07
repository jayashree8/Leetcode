'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Input: s = "leetcode"
Output: 0
'''

''' MY CODE '''
s = "aabb"
flag = 0

dict1 = {}
for i in range(len(s)):
    if s[i] not in dict1:
        dict1[s[i]] = 1
    else:
        dict1[s[i]] += 1
print(dict1)

for key, val in dict1.items():
    if val==1:
        temp = key
        flag = 1
        break

if flag==1:
    print(s.index(temp))
else:
    print("-1")