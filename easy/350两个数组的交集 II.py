from typing import List
# # 思路：暴力解法
# # 执行用时 :128 ms, 在所有 Python3 提交中击败了5.68%的用户
# # 内存消耗 :12.9 MB, 在所有 Python3 提交中击败了99.21%的用户
# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#     x = []
#     for i in nums1:
#         if i in nums2:
#             x.append(nums2.pop(nums2.index(i)))
#     return x

# 思路：同时走指针，然后比大小
# 执行用时 :56 ms, 在所有 Python3 提交中击败了85.88%的用户
# 内存消耗 :12.7 MB, 在所有 Python3 提交中击败了99.33%的用户
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    i,j = 0,0
    x = []
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            i += 1
        elif nums1[i]> nums2[j]:
            j += 1
        else:
            x.append(nums1[i])
            i += 1
            j += 1
    return x


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))