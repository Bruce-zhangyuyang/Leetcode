from typing import List
# 先找出来首尾的最大距离，然后再在中间找最大距离//2
def maxDistToClosest(seats: List[int]) -> int:
    dict_ = []
    dict_.append(seats.index(1))
    dict_.append(seats[::-1].index(1))
    for i in range(seats.index(1), len(seats) - seats[::-1].index(1)):
        if i !=len(seats)-1 and seats[i] == 1 and seats[i+1] ==0:
            j = 1
            while i+j<len(seats) and seats[i+j] == 0 :
                j = j+1
            dict_.append(j//2)
    return max(dict_)


seats = [1,0,0,0]
# seats = [0,1]
print(maxDistToClosest(seats))
