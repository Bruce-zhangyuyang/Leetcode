from typing import List
#
# # 思路：单纯的考虑隔一个，没有考虑存在相隔两个或更多的情况
# def rob(self, nums: List[int]) -> int:
#     odd = 0
#     even = 0
#     for i in range(len(nums)):
#         if i % 2 == 0:
#             even = even + nums[i]
#         else:
#             odd = odd + nums[i]
#     return max(even, odd)

# # 修正思路：引入动态规划
# def rob(nums: List[int]) -> int:
#     if len(nums) == 0: return 0
#     elif len(nums)<=2: return max(nums)
#     else:
#         for i in range(2,len(nums)):
#             nums[i] += max(nums[:i-1])
#         return max(nums)

# 方法二：动态规划二
def rob(nums: List[int]) -> int:
    if not nums: return 0
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]
    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
    return dp[-1]


nums = [1,2,3,1]
print(rob(nums))