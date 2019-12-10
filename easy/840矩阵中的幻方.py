from typing import List
# 如果grid小于3*3 直接返回0
# 否则看9个数中是否在【1，9】中 并且没有重复值 并且第一行、第一列、对角线的三个和相等
def numMagicSquaresInside(grid: List[List[int]]) -> int:
    if len(grid) <3 or len(grid[0])<3 : return 0
    num = 0
    for j in range(len(grid[0])-2):
        for i in range(len(grid)-2):
            lis_ = [grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], \
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
            if (grid[i][j]+grid[i+1][j]+grid[i+2][j]) == (grid[i][j]+grid[i][j+1]+grid[i][j+2])\
                    == (grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]) and \
                    len(set(lis_)) == 9 and max(lis_) <=9 and min(lis_) >0:
                num+=1
    return num


grid = [[7,0,5],[2,4,6],[3,8,1]]

a = numMagicSquaresInside(grid)
print(a)