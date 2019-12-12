from typing import List
# 版本1思路： 把所有元素的位置做成字典 然后组合 两两相减 如果有满足条件的 return True
# def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
#     if len(nums)<2: return False
#     from itertools import combinations
#     set_ = set(nums)
#     for i in set_:
#         dict_ = {}
#         for j in range(len(nums)):
#             if nums[j] == i:
#                 if i not in dict_:
#                     dict_[i] = [j]
#                 else:
#                     dict_[i].append(j)
#         if len(dict_[i])>=2:
#             result = list(combinations(dict_[i], 2))
#             for a, b in result:
#                 if abs(a - b) <= k:
#                     return True
#     return False

# 版本2思路： 直接把前一个索引放到字典里面 要是不满足直接替换 满足return False 但还是分元素看
# def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
#     if len(nums)<2: return False
#     set_ = set(nums)
#     for i in set_:
#         dict_ = {}
#         for j in range(len(nums)):
#             if nums[j] == i:
#                 if i in dict_ and abs(j - dict_[i]) <= k:
#                     return True
#                 else:
#                     dict_[i] = j
#     return False
# 版本3思路： 直接遍历
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    dict_ = {}
    for j in range(len(nums)):
        if nums[j] in dict_:
            if abs(dict_[nums[j]] - j)<=k:
                return True

        dict_[nums[j]] = j
    return False



# nums = [1,2,3,1]
# k = 3
# nums = [99,99]
# k = 2
nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))