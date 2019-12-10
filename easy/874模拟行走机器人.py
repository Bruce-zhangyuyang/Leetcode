from typing import List

#思路： 先把所有障碍物的位置存入字典，然后机器人走路 ，查看路线中是否存在障碍物

def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    loc = [['y', 1], ['x', 1], ['y', -1], ['x', -1]]
    x= 0
    a = 0
    b = 0
    o = 0
    x2y, y2x = {}, {}
    for n,m in obstacles:
        if n not in x2y:
            x2y[n] = [m]
        else:
            x2y[n].append(m)
        if m not in y2x:
            y2x[m] = [n]
        else:
            y2x[m].append(n)
    for i in commands:
        r = 0
        t = []
        if i == -1:
            x = (x+1) % 4
        elif i == -2:
            x = (x-1) % 4
        if loc[x][0] == 'x' and loc[x][1] > 0 and i > 0:
            if b in y2x:
                p = set(y2x[b]) & set([e for e in range(a+1, a+i+1)])
                if p:
                    t.append(min(p)-1)
                    r = 1
            if r == 0:
                a += i
            if r == 1:
                a = min(t)
        if loc[x][0] == 'x' and loc[x][1] < 0 and i > 0:
            if b in y2x:
                p = set(y2x[b]) & set([e for e in range(a-i, a)])
                if p:
                    t.append(max(p) + 1)
                    r = 1
            if r == 0:
                a -= i
            if r == 1:
                a = max(t)
        if loc[x][0] == 'y' and loc[x][1] > 0 and i > 0:
            if a in x2y:
                p = set(x2y[a]) & set([e for e in range(b+1, b+i+1)])
                if p:
                    t.append(min(p) - 1)
                    r = 1
            if r == 0:
                b +=i
            if r == 1:
                b = min(t)
        if loc[x][0] == 'y' and loc[x][1] < 0 and i > 0:
            # obs = [ob[1] for ob in obstacles if ob[0] == a]
            if a in x2y:
                p = set(x2y[a]) & set([e for e in range(b - i, b)])
                if p:
                    t.append(min(p) + 1)
                    r = 1
            if r == 0:
                b -= i
            if r == 1:
                b = max(t)
        o = max(o, a**2 + b**2)
    return o


commands = [4,-1,4,-2,4]

obstacles = [[2,4]]
a = robotSim(commands, obstacles)
print(a)