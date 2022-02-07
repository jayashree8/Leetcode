'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
'''

s = "anagram"
t = "nagaram"

dict1 = {}
dict2 = {}

for i in range(len(s)):
    if s[i] not in dict1:
        dict1[s[i]] = 1
    else:
        dict1[s[i]] += 1

for i in range(len(t)):
    if t[i] not in dict2:
        dict2[t[i]] = 1
    else:
        dict2[t[i]] += 1