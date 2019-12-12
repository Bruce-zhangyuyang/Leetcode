# 思路：先把所有符号变为’ ‘， 然后分词 接着统计
from typing import List
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.lower()
    for i in [",", ".", "!", "?", "'", ";"]:
        paragraph = paragraph.replace(i, ' ')
    print(paragraph)
    paragraph = paragraph.split()
    from collections import Counter
    b = Counter(paragraph)
    c = sorted(b.values())[::-1]
    for k in c:
        for x in b:
            if x not in banned and b[x] == k:
                return x
    return ''


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph, banned))