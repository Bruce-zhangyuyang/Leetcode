from typing import List
def isBoomerang(points: List[List[int]]) -> bool:
    from itertools import combinations
    for a, b in combinations(points, 2):
        if a == b:
            return False
    if (points[1][1] - points[0][1]) * (points[2][0] - points[0][0])  != \
            (points[2][1] - points[0][1]) * (points[1][0] - points[0][0]):
        return True
    else:
        return False


# points = [[1,1],[2,2],[0,0]]
# points = [[1,1],[2,3],[3,2]]
# points = [[2,1],[0,1],[0,1]]
# points = [[0,1],[1,1],[2,1]]
points = [[0,0],[0,2],[2,1]]
print(isBoomerang(points))