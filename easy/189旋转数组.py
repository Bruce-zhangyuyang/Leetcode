from typing import List
# 思路：先把前后两边的进行倒序， 然后再对整体进行倒序
def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    nums[n-k:] = nums[n-k:][::-1]
    nums[:n-k] = nums[:n-k][::-1]
    nums[:] = nums[::-1] # 这里要加上[:] 否则电脑会认为重新声明了一个
    return nums


nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))
