from typing import List
# 思路：先变成数字 然后加一 再变成列表
def plusOne(digits: List[int]) -> List[int]:
    sum = 0
    for i in digits:
        sum = sum*10 + i
    x = [j for j in str(sum+1)]
    return x


digits = [1,2,3]
print(plusOne(digits))