from typing import List
# # 思路：理解错误，认为出现以后只是单纯的加起来，没想到是组合
# def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
#     # sa_num = len(dominoes) - len(list(set(dominoes)))
#     re_do = []
#     for i in dominoes:
#         re_do.append(tuple(i[::-1]))
#         re_do.append(tuple(i))
#     sa_num = int((len(re_do) - len(list(set(re_do))))/2)
#     return sa_num
# # 思路2：暴力解法
# def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
#     from itertools import combinations
#     w = 0
#     for a, b in combinations(dominoes,2):
#         if a == b or a ==b[::-1]:
#             w += 1
#     return w

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    s = {}
    for a in dominoes:
        x = tuple(sorted(a))
        if x not in s:
            s[x] = 1
        else:
            s[x] += 1
    tol = 0
    for c in s.values():
        tol += c* (c-1)/2
    return int(tol)

# dominoes = [[1,2],[2,1],[3,4],[5,6],[1,2],[3,4]]
dominoes = [[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]
print(numEquivDominoPairs(dominoes))