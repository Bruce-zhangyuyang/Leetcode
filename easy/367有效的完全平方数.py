# 思路：二分法寻找平方根
# 执行用时 :28 ms, 在所有 python3 提交中击败了97.30%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户
def isPerfectSquare(num: int) -> bool:
    start = 0
    end = num
    while start <= end:
        mid = (start + end)//2
        print(mid)
        if mid**2 > num:
            end = mid - 1
        elif mid**2 <num:
            start = mid + 1
        elif mid**2 == num:
            return True
    return False

num = 10000
print(isPerfectSquare(num))