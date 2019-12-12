from typing import List
# 思路：列举所有情况
def numMovesStones(a: int, b: int, c: int) -> List[int]:
    q = [a,b,c]
    q = sorted(q)
    x = q[0]
    z = q[2]
    y = q[1]
    if x+1 == y and y+1 == z :return [0, 0]
    elif x+1 == y or y+1 == z:
        return [1, max(y-x-1, z-y-1)]
    elif x+2 == y or y+2 == z:
        return [1, z-x-2]
    else:
        return [2, z-x-2]


# a = 1
# b = 2
# c = 5
a = 4
b = 3
c = 2
print(numMovesStones(a, b, c))
