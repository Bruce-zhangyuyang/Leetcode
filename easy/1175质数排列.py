# 思路：找出所有的质数和合数的个数 然后阶乘
def numPrimeArrangements(n: int) -> int:
    prime, com = [], [1]
    if n < 2: return 1
    num = [i for i in range(2, n+1)]
    while num != []:
        x = num.pop(0)
        prime.append(x)
        for i in range(n//x + 1):
            if x * i in num:
                com.append(x * i)
                num.remove(x * i)
    num_p = len(prime)
    num_c = len(com)
    c_p = 1
    c_c = 1
    for i in range(1,num_p + 1):
        c_p *= i
    for i in range(1,num_c + 1):
        c_c *= i
    return (c_p * c_c) % (10**9 + 7)

n = 100
print(numPrimeArrangements(n))
