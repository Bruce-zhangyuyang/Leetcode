from typing import List
# 思路：用Counter生成字典 然后计算最长和谐子序列
def findLHS(nums: List[int]) -> int:
    le = 0
    from collections import Counter
    dic = Counter(nums)
    for i in dic:
        if i + 1 in dic:
            k = dic[i] + dic[i + 1]
        else:
            continue
        le = max(le, k)
    return le


nums = [1,3,2,2,5,2,3,7]
print(findLHS(nums))