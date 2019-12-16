from typing import List
# 思路：另外生成一个列表， 进行排序最大的和第二大的两倍进行比较 如果只有一个数 则返回0
def dominantIndex(nums: List[int]) -> int:
    if len(nums)<2: return 0
    li = sorted(nums)[::-1]
    if li[0]>=2 * li[1]:
        return nums.index(li[0])
    else:
        return -1


# nums = [1, 2, 3, 4]
# nums = [3, 6, 1, 0]

print(dominantIndex(nums))
