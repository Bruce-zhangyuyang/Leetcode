# # 暴力解法：超出时间限制
# def trailingZeroes(n: int) -> int:
#     import math
#     value = str(math.factorial(n))
#     return len(value) - len(value.rstrip('0'))

# 思路：找到n的里面有多少个5， 结果：超出时间限制
def trailingZeroes(n: int) -> int:
    if n<5: return 0
    w = 0
    for i in range(5, n+1, 5):
        while i%5 == 0:
            w += 1
            i = i//5
    return w

# 思路：100里面有20个5，其中25中有两个5（有4个25），
def trailingZeroes(n: int) -> int:
    i = 5
    num = 0
    while n>=i:
        num += n//i
        i = i * 5
    return num



n = 1001

print(trailingZeroes(n))
