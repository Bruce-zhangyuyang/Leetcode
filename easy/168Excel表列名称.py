# 思路：要是能被26整除 则加上26的倍数然后再跟27 取余
def convertToTitle(n: int) -> str:
    res = ''
    s = 0
    if n == 1 : return 'A'
    while n > 0:
        if n %26  == 0:
            res = chr(64 + (n+(n//26)-1) % 27) + res
            n = n // 27
        else:
            res = chr(64+(n) % 26) + res
            n = n//26
        s += 1
    return res


n = 78
print(convertToTitle(n))
