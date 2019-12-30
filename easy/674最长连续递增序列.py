from typing import List
# # 执行用时 :144 ms, 在所有 python3 提交中击败了6.73%的用户
# # 内存消耗 :13.9 MB, 在所有 python3 提交中击败了95.48%的用户
# def findLengthOfLCIS(nums: List[int]) -> int:
#     num = 1
#     nu = []
#     if not nums: return 0
#     for i in range(len(nums)-1):
#         if nums[i] < nums[i+1]:
#             num += 1
#         else:
#             nu.append(num)
#             num = 1
#     nu.append(num)
#     return max(nu)

def findLengthOfLCIS(nums: List[int]) -> int:
    hash_dict = dict()

    max_length = 0
    for num in nums:
        if num not in hash_dict:
            left = hash_dict.get(num - 1, 0)
            right = hash_dict.get(num + 1, 0)

            cur_length = 1 + left + right
            if cur_length > max_length:
                max_length = cur_length

            hash_dict[num] = cur_length
            hash_dict[num - left] = cur_length
            hash_dict[num + right] = cur_length

    return max_length


nums = [1,2,3,6,4,5,7]
print(findLengthOfLCIS(nums))