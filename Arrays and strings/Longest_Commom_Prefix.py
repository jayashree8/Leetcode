'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

''' MY CODE'''
strs = ["flower","flow","flight"]
output = []

num = len(strs)

for i in zip(*strs):
    if(len(set(i))==1):
        output.append(i[0])
    else:
        break

print("".join(output))

    
