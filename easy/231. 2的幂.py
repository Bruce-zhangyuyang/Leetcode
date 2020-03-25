# # 思路1： 暴力解锁，控制小数位数
# def isPowerOfTwo(n: int) -> bool:
#     import math
#     s = int(math.log(n, 10))
#     result = round(math.log(n, 2), s + 3)
#     print(result)
#     return int(result) == result

# 思路：二进制种所有2的幂次方都是最高位是1 其他都是0
def isPowerOfTwo(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0

n = 536870912
print(isPowerOfTwo(n))
