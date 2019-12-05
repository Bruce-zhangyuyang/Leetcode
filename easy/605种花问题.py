from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    loc = [k for k,v in enumerate(flowerbed) if v ==1]
    if not loc:
        x = (len(flowerbed)+1)//2
        return x>=n
    x = loc[0]//2 + (len(flowerbed)-loc[-1]-1)//2
    loc_ = [loc[i+1]-loc[i]-1 for i in range(len(loc)-1) if loc[i+1]-loc[i]>2]
    for i in loc_:
        x+= (i-1)//2
    return x>=n

# flowerbed = [1,0,0,0,1,1,1,1,0,1,1,0,0,0]
n = 2
# flowerbed = [1,0,0,0,0,1]
flowerbed = [0]
a = canPlaceFlowers(flowerbed, n)
print(a)

[0, 4, 5, 6, 7, 9, 10, 11, 12, 13]