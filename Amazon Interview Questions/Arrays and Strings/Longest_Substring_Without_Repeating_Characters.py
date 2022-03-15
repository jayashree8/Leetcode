'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

s = "pwwkew"

''' MY CODE '''
substr = []
dict1 = {}
maxlen = 0

for i in s:
    while i in dict1:
        letter = substr.pop(0)
        dict1.pop(letter)
    substr.append(i)
    dict1[i] = i
    dictlen = len(dict1)
    if maxlen<dictlen:
        maxlen = dictlen

print(maxlen)

