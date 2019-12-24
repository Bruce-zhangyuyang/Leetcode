def firstUniqChar(s: str) -> int:
    from collections import Counter
    dic = Counter(s)
    for i in s:
        if dic[i] == 1:
            return s.index(i)
    return -1



s = "leetcode"
print(firstUniqChar(s))