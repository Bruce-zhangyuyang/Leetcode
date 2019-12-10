from typing import List


# def findPairs(nums: List[int], k: int) -> int:
#     if len(nums) <2 : return 0
#     num = 0
#     li_ = []
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if abs(nums[i] - nums[j]) == k and [nums[i], nums[j]] not in li_:
#                 li_.append([nums[i], nums[j]])
#                 li_.append([nums[j], nums[i]])
#                 num += 1
#     return num

# 思路1：如果列表中个数小于2 或者差的绝对值小于0 则返回0
#        否则就将列表中本元素删除 然后找到符合条件的 并且对没有出现过的排列进行计数 最后+1除以2取整

# def findPairs(nums: List[int], k: int) -> int:
#     if len(nums) < 2 or k < 0: return 0
#     num_ = 0
#     dict_ = {}
#     for i in nums:
#         dict_[i] = ['0']
#     for i in range(len(nums)):
#         snum = nums.copy()
#         snum.remove(snum[i])
#         if k == 0 and nums[i] not in dict_[nums[i]] and nums[i] in snum:
#             num_+=2
#             dict_[nums[i]].append(nums[i])
#         else:
#             if (nums[i]+k) in snum and (nums[i]+k) not in dict_[nums[i]]:
#                 num_+=1
#                 dict_[nums[i]].append(nums[i]+k)
#             if (nums[i]-k) in snum and (nums[i]-k) not in dict_[nums[i]]:
#                 num_+=1
#                 dict_[nums[i]].append(nums[i]-k)
#     print(dict_)
#     return (num_+1)//2

# 思路： 寻找所有满足条件的数字，并且将满足条件的两个数字中大的 添加到b

def findPairs(nums: List[int], k: int) -> int:
    if len(nums) < 2 or k < 0: return 0
    a,b = set(), set()
    for n in nums:
        if (n+k) in a:
            b.add(n+k)
        if (n-k) in a:
            b.add(n)
        a.add(n)
    print(b)
    return len(b)

nums = [3, 1, 4, 1, 5]
k = 2
a = findPairs(nums, k)
print(a)

s, r = set(), set()

