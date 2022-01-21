'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
Input: haystack = "hello", needle = "ll"
Output: 2
'''
haystack = "hello"
needle = "ll"

output = haystack.find(needle)
print(output)
