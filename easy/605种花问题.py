from typing import List
# 思路1： 找到所有种花的位置 如果没有种花 则（整个花坛长度+1）//2 然后与所需种的花的个数进行比较
        如果已经种花，则先把最前面以及最后面能够种的花的个数统计出来，然后

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    loc = [k for k,v in enumerate(flowerbed) if v ==1]
    if not loc:
        x = (len(flowerbed)+1)//2
        return x>=n
    x = loc[0]//2 + (len(flowerbed)-loc[-1]-1)//2
    loc_ = [loc[i+1]-loc[i]-1 for i in range(len(loc)-1) if loc[i+1]-loc[i]>2] # loc[i+1]-loc[i]-1：记录中间有多少个空位
    for i in loc_:
        x+= (i-1)//2 # 3，4都是只能种一朵花
    return x>=n

# flowerbed = [1,0,0,0,1,1,1,1,0,1,1,0,0,0]
n = 2
# flowerbed = [1,0,0,0,0,1]
flowerbed = [0]
a = canPlaceFlowers(flowerbed, n)
print(a)

[0, 4, 5, 6, 7, 9, 10, 11, 12, 13]