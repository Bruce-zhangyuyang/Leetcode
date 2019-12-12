from typing import List
# 错误思路：有最大值的不一定就是最大的 我蠢了
# def findMaxAverage(nums: List[int], k: int) -> float:
#     b = []
#     for i in range(len(nums)):
#         if nums[i] == max(nums):
#             b.append(i)
#     print(b)
#     s = []
#     for a in b:
#         min_ = max(a - k + 1,0)
#         max_ = min(a + k, len(nums))
#         for i in range(min_, max_-k+1):
#             s.append(sum(nums[i:i+k]))
#     return max(s) / k

def findMaxAverage(nums: List[int], k: int) -> float:
    result_ = sum(nums[:k])
    max_ = 0
    for i in range(k, len(nums)):
        result_ = result_+nums[i]-nums[i-k]
        max_ = max(max_, result_)
    return max_/k
# nums = [1,12,-5,-6,50,3]
# k = 4
# nums = [8,0,1,7,8,6,5,5,6,7]
# k = 5
# nums = [5]
# k = 1
nums = [0,4,0,3,2]
k = 1
print(findMaxAverage(nums, k))