from typing import List
# 暴力解法： 超出时间限制
# def findErrorNums(nums: List[int]) -> List[int]:
#     x = []
#     for i in range(1, len(nums) + 1):
#         if i not in nums:
#             x.append(i)
#         else:
#             nums.remove(i)
#     x.append(nums[0])
#     return x[::-1]

def findErrorNums(nums: List[int]) -> List[int]:
    x = set([i for i in range(1, len(nums)+1)])
    nums_ = set(nums)
    from collections import Counter
    s = Counter(nums)
    q = list(x - nums_)
    for k, v in s.items():
        if v == 2:
            q.append(k)
            return q[::-1]



nums = [1,2,2,4]
# nums = [1,2,3,4,5,5,7,8]
# nums = [1, 1]
# nums = [1,3,3]
# nums = [3,2,3,4,6,5]
print(findErrorNums(nums))