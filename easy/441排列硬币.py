# 思路： 暴力解法： 时间超出限制
def arrangeCoins(n: int) -> int:
    if n < 2: return n
    sum_ =  sum(range(n//2 + 1))
    i = n//2
    while sum_ > n:
        sum_ -= i
        i -= 1
    return i

# 思路：k(k+1)/2 == n 倒推并对k取整
def arrangeCoins(n: int) -> int:
    import math
    return int(math.sqrt(2 * n + 0.25) - 0.5)

n = 5
print(arrangeCoins(n))