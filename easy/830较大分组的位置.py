from typing import List
# 思路：两个指针 一个指着原位置 一个指着与原位置相同字母的最远位置
def largeGroupPositions(S: str) -> List[List[int]]:
    s = 0
    x = []
    while s<len(S):
        j = 1
        while s+j < len(S) and S[s+j] == S[s]:
            j += 1
        print(S[s], j)
        if j>=3:
            x.append([s, s+j-1])
        s += j
    return x



S = "abcdddeeeeaabbbcd"
print(largeGroupPositions(S))