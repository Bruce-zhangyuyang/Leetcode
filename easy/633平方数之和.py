# 思路： 从0到c的平方根之间，寻找是否是两个数的平方和

def judgeSquareSum(c: int) -> bool:
    if c == 0: return True
    for i in range(int(c**0.5)+1):
        if ((c-i**2)**0.5)%1 == 0:
            print(i)
            return True
    return False


c = 99999999
a = judgeSquareSum(c)
print(a)