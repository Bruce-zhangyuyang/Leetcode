from typing import List

# 思路1： 寻找一个数后面比他小的数的位置 以及前面比他大的数的位置 最后将最后面的位置 减去最前面的位置

# def findUnsortedSubarray(nums: List[int]) -> int:
#     s = []
#     i = 0
#     while i <= len(nums) -1:
#         g = 1
#         h = 1
#         while i+g <= len(nums) - 1 and nums[i] > nums[i+g] :
#             s.append(i)
#             s.append(i+g)
#             g += 1
#         while i-h >=0 and nums[i-h] > nums[i]:
#             s.append(i-h)
#             s.append(i)
#             h +=1
#         i += 1
#     if s:
#         return (max(s) - min(s) + 1)
#     else:
#         return 0

# 思路2： 生成一张排序的表 然后与原表对比 记录不同的位置编号 直接最大的减去最小的

def findUnsortedSubarray(self, nums: List[int]) -> int:
    s = []
    nums_ = sorted(nums)
    for i in range(len(nums)):
        if nums_[i] !=nums[i]:
            s.append(i)
    if s:
        return s[-1] - s[0] +1
    else:
        return 0

nums = [2, 6, 4, 8, 10, 9, 15]
# 5
# nums = [1,3,2,2,2]
# 4
# nums = [2,3,3,2,4]
# 3
# nums = [1,2,4,5,3]
# 3
print(findUnsortedSubarray(nums))