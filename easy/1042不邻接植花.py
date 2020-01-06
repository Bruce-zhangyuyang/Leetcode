from typing import List
# 思路： 暴力解法

# def gardenNoAdj(N: int, paths: List[List[int]]) -> List[int]:
#     s = [1] * N
#     x = 0
#     step = 0
#     paths = sorted(paths)
#     while x < len(paths):
#         p = sorted(paths[step])
#         if s[p[0]-1] == s[p[1]-1]:
#             x = 0
#             if s[p[1]-1] < 4:
#                 s[p[1]-1] += 1
#             else:
#                 s[p[1]-1] -= 1
#         else:
#             x += 1
#         step += 1
#         if step >= len(paths):
#             step = int(step % len(paths))
#     return s


# 思路：因为一定有路径 所以直接把所有链接的取值剔除掉
def gardenNoAdj(N: int, paths: List[List[int]]) -> List[int]:
    res=[0]*N
    G=[[] for _ in range(N)]
    for x,y in paths:
        G[x-1].append(y-1)
        G[y-1].append(x-1)
    for i in range(N):
        l = {res[j] for j in  G[i]}
        res[i]=({1,2,3,4}-{res[j] for j in G[i]}).pop()
    return res

# N = 3
# paths = [[1,2],[2,3],[3,1]]
# N = 4
# paths = [[1,2],[3,4]]
# N = 4
# paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
N = 8
paths = [[1,7],[5,4],[2,8],[7,5],[2,4],[2,7],[4,3],[5,1],[3,1]]
print(gardenNoAdj(N, paths))