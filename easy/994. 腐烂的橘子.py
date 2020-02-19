from typing import List
def orangesRotting(grid: List[List[int]]) -> int:
    from collections import deque
    que = deque()
    loc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    width = len(grid[0])
    length = len(grid)
    for i in range(length):
        for j in range(width):
            if grid[i][j] == 2:
                que.append((i, j, 0))
    cnt = 0
    while que:
        print(f'第{cnt}状态：{que}')
        x, y, time = que.popleft()
        for lo in loc:
            x_ = x + lo[0]
            y_ = y + lo[1]
            if 0<= x_<= width -1 and 0<= y_<= length -1 and grid[x_][y_] == 1:
                grid[x_][y_] = 2
                que.append((x_, y_, time+1))
        cnt += 1
    if any(1 in row for row in grid):
        return -1
    return time


# grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))