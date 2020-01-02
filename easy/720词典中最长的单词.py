from typing import List
# 思路：先进行排序 然后从最长的开始进行遍历找看该单词是否由words词典中其他单词逐步添加一个字母组成。
def longestWord(words: List[str]) -> str:
    words = sorted(words)
    words.sort(key=len,reverse=True)
    for word in words:
        re = True
        for i in range(1, len(word)+1):
            if word[:i] not in words:
                re = False
                break
        if re:
            return word
    return ''


words = ["a","banana","app","appl","ap","apply","apple"]
print(longestWord(words))

