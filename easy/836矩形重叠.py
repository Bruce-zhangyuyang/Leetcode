from typing import List
# 思路：排除不可能
def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
    return not(
        rec2[2]<=rec1[0]or\
        rec2[3]<=rec1[1]or\
        rec2[0]>=rec1[2]or\
        rec2[1]>=rec1[3]
    )

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print(isRectangleOverlap(rec1, rec2))