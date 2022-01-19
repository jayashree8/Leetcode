'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''
''' MY CODE'''
digits = [9]

def plusOne(digits):
    val = int("".join(map(str, digits)))
    summ = val+1
    res = list(map(int, str(summ)))
    return res

print(plusOne(digits))