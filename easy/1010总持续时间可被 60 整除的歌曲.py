from typing import List
# 思路：暴力解法 超出时间限制
# def numPairsDivisibleBy60(time: List[int]) -> int:
#     from itertools import combinations
#     num = 0
#     for a, b in combinations(time, 2):
#         if (a + b)%60 == 0:
#             num += 1
#     return num


# 思路：找能与time[i] 相加等于60 的数的个数
def numPairsDivisibleBy60(time: List[int]) -> int:
    temp = [0] * 60
    n = 0
    for i in range(len(time)):
        n += temp[(60 - (time[i] % 60)) % 60]
        temp[time[i] % 60] += 1
    return n


time = [60,60,60]
print(numPairsDivisibleBy60(time))
