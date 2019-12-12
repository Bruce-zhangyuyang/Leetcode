
# 思路： 从0到根号num +1 看num 的因子 将其相加与num 判断是否相等
def checkPerfectNumber(num: int) -> bool:
    if num <2 :return False
    set_ = set([1])
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            set_.add(i)
            set_.add(num//i)
    return num == sum(set_)


num = 9
print(checkPerfectNumber(num))