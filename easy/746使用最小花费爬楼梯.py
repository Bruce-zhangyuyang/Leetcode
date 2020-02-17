from typing import List
# 思路：动态规划
# 执行用时 :64 ms, 在所有 Python3 提交中击败了88.31%的用户
# 内存消耗 :12.9 MB, 在所有 Python3 提交中击败了98.60%的用户
def minCostClimbingStairs(cost: List[int]) -> int:
    cost.append(0)
    if len(cost) < 3 : return min(cost)
    for i in range(2, len(cost)):
        cost[i] = cost[i] + min(cost[i-1], cost[i-2])
    return cost[-1]


# cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))