'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

''' MY CODE s'''
s = "Let's take LeetCode contest"

lst = s.split(" ")
print(lst)

output = []
for i in lst:
    output.append(i[::-1])

print(" ".join(output))