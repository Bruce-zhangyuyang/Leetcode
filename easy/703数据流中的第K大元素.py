from typing import List
# 思路：找到第k大的数，只要add比他小，就一直输出他   超出时间限制
# 修改：把nums进行截断，只留下前k大的数，减少运算时间   超出时间限制
# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = sorted(nums)
#         self.n = -10000000
#         if len(self.nums) > self.k:
#             self.n = self.nums[- self.k]
#             self.nums = self.nums[- self.k:]
#
#     def add(self, val: int) -> int:
#         if len(self.nums) < self.k:
#             self.nums.append(val)
#             self.n = sorted(self.nums)[- self.k]
#             return self.n
#         elif val < self.n:
#             return self.n
#         else:
#             self.nums.append(val)
#             self.n = sorted(self.nums)[- self.k]
#             return sorted(self.nums)[- self.k]
#
#     # Your KthLargest object will be instantiated and called as such:
#     # obj = KthLargest(k, nums)
#     # param_1 = obj.add(val)

import heapq
# 思路：参考网上的答案，加入heapq，这样可以直接进行判断，并且如果出现比当前第k大的值大的数，可以直接使用heapreplace进行替换，速度很快
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = heapq.nlargest(self.k, nums)
        print(self.nums)
    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]
nums = []
k = 1
val = [-3,-2,-4,0,4]
obj = KthLargest(k, nums)
for i in val:
    param_1 = obj.add(i)
    print(param_1)

for a, b in en