digits = [9]

def plusOne(digits):
    val = int("".join(map(str, digits)))
    summ = val+1
    res = list(map(int, str(summ)))
    return res

print(plusOne(digits))