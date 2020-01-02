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

# def findErrorNums(nums: List[int]) -> List[int]:
#     x = set([i for i in range(1, len(nums)+1)])
#     nums_ = set(nums)
#     from collections import Counter
#     s = Counter(nums)
#     q = list(x - nums_)
#     for k, v in s.items():
#         if v == 2:
#             q.append(k)
#             return q[::-1]

# 执行用时 :240 ms, 在所有 python3 提交中击败了68.78%的用户
# 内存消耗 :15.5 MB, 在所有 python3 提交中击败了5.21%的用户
def findErrorNums(nums: List[int]) -> List[int]:
    x = set([i for i in range(1, len(nums)+1)])
    nums_ = set(nums)
    from collections import Counter
    s = Counter(nums).most_common(1)
    q = list(x - nums_)
    q.append(s[0][0])
    return q


nums = [1,2,2,4]
# nums = [1,2,3,4,5,5,7,8]
# nums = [1, 1]
# nums = [1,3,3]
# nums = [3,2,3,4,6,5]
print(findErrorNums(nums))