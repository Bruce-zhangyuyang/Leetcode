from typing import List
# 思路1： 从右边开始将所有的和以及他的索引放入字典 然后从0开始查
# def pivotIndex(nums: List[int]) -> int:
#     dict_ = {}
#     for j in range(len(nums)+1)[::-1]:
#         if sum(nums[j:]) not in dict_:
#             dict_[sum(nums[j:])] = [j]
#         else:
#             dict_[sum(nums[j:])].append(j)
#     dict_1 = {}
#     for i in range(0, len(nums)+1):
#         dict_1[i] == sum(nums[:i])
#     for i in range(0, len(nums)+1):
#         if dict_1[i] in dict_ and i+1 in dict_[sum(nums[:i])]:
#             return i
#     else: return -1

# # 思路2： 假设左边部分已经满足等于右边 则左边部分*2+nums[i] 就正好等于sum(nums)
# def pivotIndex(nums: List[int]) -> int:
#     sum_ = sum(nums)
#     left_sum = 0
#     for i in range(len(nums)-1):
#         if left_sum *2 + nums[i] == sum_:
#             return i
#         left_sum += nums[i]
#     return -1

#  思路3： 暴力解锁
def pivotIndex(nums: List[int]) -> int:
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i

    return -1


nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
# nums = [-1,-1,-1,-1,-1,0]
# nums = [-1,-1,-1,0,1,1]
# nums = [-1,-1,0,-1,-1,0]
# nums = [-1,-1,0,1,1,0]
print(pivotIndex(nums))