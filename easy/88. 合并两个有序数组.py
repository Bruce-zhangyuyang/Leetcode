
from typing import List
# def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # nums1[:] = sorted(nums1[:m] + nums2) # 一句话 但是用时长


# 执行用时 :92 ms, 在所有 Python3 提交中击败了6.79%的用户
# 内存消耗 :28.8 MB, 在所有 Python3 提交中击败了5.35%的用户
# 思路：不断的往后走 效率有所提升 但麻烦
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # nums1[:] = sorted(nums1[:m] + nums2)
    x = 0
    y = 0
    nums1[:] = nums1[:m]
    while x < n and y < len(nums1):
        if nums2[x] <= nums1[y]:
            nums1.insert(y, nums2[x])
            y += 1
            x += 1
        else:
            y += 1
    while x < n:
        nums1.insert(y, nums2[x])
        y += 1
        x += 1
nums1 = [1,2,3]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))

