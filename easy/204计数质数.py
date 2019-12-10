# 按照所含的数字造一张全是 1 的表 然后将所有的合数全部标记为0 最后求 表的总和


def countPrimes(n: int) -> int:
    x = [1] * n
    if n < 3:
        return 0
    x[0] = x[1] = 0
    for i in range(2, n):
        if x[i] == 1:
            num = 2
            while i * num < n:
                x[i * num] = 0
                num += 1
    return sum(x)




n = 10
a = countPrimes(n)
print(a)