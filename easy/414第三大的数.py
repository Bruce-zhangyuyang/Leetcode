from typing import List

# 思路： 先去重并且排序 如果长度小于3则返回最大的 不然就返回第三大的数字

def thirdMax(nums: List[int]) -> int:
    s = list(sorted(set(nums)))
    if len(s)>=3:
        return s[-3]
    else:
        return s[-1]

nums = [2, 2, 3, 1]
print(thirdMax(nums))