from typing import List
# # 暴力解法：
# # 执行用时 :2364 ms, 在所有 python3 提交中击败了5.09%的用户
# # 内存消耗 :13.7 MB, 在所有 python3 提交中击败了27.92%的用户
# def addToArrayForm(A: List[int], K: int) -> List[int]:
#     num = 0
#     for i in A:
#         num = num * 10 + i
#     num += K
#     s = []
#     if num == 0:
#         return [0]
#     while num > 0:
#         s.append(num % 10)
#         num = num//10
#     return s[::-1]


def addToArrayForm(A: List[int], K: int) -> List[int]:
    A = [str(x) for x in A]
    return [int(x) for x in str(int(''.join(A)) + K)]


A = [0]
K = 0
print(addToArrayForm(A, K))