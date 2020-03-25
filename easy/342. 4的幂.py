# # 思路： 4**(x) = 2**(2x)
# def isPowerOfFour(num: int) -> bool:
#     from math import log2
#     return num > 0 and log2(num) % 2 == 0

def isPowerOfFour(num: int) -> bool:
    return num > 0 and num & (num - 1) == 0 and num % 3 == 1

num = 4
print(isPowerOfFour(num))