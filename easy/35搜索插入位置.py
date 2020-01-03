from typing import List
# 执行用时 :60 ms, 在所有 Python3 提交中击败了77.78%的用户
# 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了95.67%的用户
def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end)//2
        if nums[mid] == target: return mid
        elif nums[mid]>target:
            end = mid -1
        elif nums[mid]< target:
            start = mid + 1
    return start

nums =[0,1,2,3]
target = 2
print(searchInsert(nums, target))