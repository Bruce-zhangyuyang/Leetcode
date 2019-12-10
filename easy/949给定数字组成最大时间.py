from typing import List

# 思路： 先将所有情况排列组合 然后时<=23 分<=59 并且时的数字不能出现在分 小于10的数字要前面补0
def largestTimeFromDigits(A: List[int]) -> str:
    a = sorted(A)
    if a[0] >2 or a[-1]>9 or a[0]<0: return ''

    from itertools import combinations
    com_list = list(combinations(a,2))
    x = []
    for s in com_list:
        x.append(s[0]*10 + s[1])
        x.append(s[1]*10 + s[0])
    x = sorted(x)[::-1]
    for i in x:
        q = a.copy()
        if i <24:
            if i%10 in q:
                q.remove(i%10)
            if i//10 in q:
                q.remove(i//10)
            if q:
                if q[-1]<=5:
                    b = q[-1]*10 + q[0]
                    if i < 10:
                        i = f'0{i}'
                    if b<10:
                        b = f'0{b}'
                    return f'{i}:{b}'
                elif q[0]<=5:
                    b = q[0]*10 + q[-1]
                    if i<10:
                        i = f'0{i}'
                    if b<10:
                        b = f'0{b}'
                    return f'{i}:{b}'
    return ''




A = [0,0,0,0]
# A = [8,2,2,6]
# A = [0,0,1,0]
# A = [0,4,0,3]
print(largestTimeFromDigits(A))
