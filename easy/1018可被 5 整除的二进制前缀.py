from typing import List
# # 执行用时 :376 ms, 在所有 python3 提交中击败了67.91%的用户
# # 内存消耗 :13.8 MB, 在所有 python3 提交中击败了100.00%的用户
# # 思路：每次累加进去 有一种动态递归的感觉
# def prefixesDivBy5(A: List[int]) -> List[bool]:
#     s = []
#     k = 0
#     for i in A:
#         k = k*2 + i
#         if k%5 == 0:
#             s.append(True)
#         else:
#             s.append(False)
#     return s

# 思路2： 简化代码 和上面没有任何区别
def prefixesDivBy5(A: List[int]) -> List[bool]:
    s = []
    k = 0
    for i in A:
        k = k*2 + i
        s.append(k%5 == 0)
    return s


A = [0,1,1,1,1,1]
print(prefixesDivBy5(A))