# 思路：根据数字的个数来近似小数位数
def isPowerOfThree(n: int) -> bool:
    import math
    n_ = int(math.log10(n))
    print(n_)
    num = round(math.log(n, 3), n_+4)
    print(num)
    return int(num) == num

n = 243
print(isPowerOfThree(n))