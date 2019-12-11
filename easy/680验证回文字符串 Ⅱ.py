# def validPalindrome(s: str) -> bool:
#     if s == s[::-1]: return True
#     x = []
#     p = 0
#     for i in range(len(s)):
#         x.append(s[i])
#     from itertools import combinations
#     c = list(combinations(x,len(s)-1))
#     for d in c:
#         if d == d[::-1]:
#             return True
#     return False


# 思路： 从头尾两边开始走 找到不一样的位置 然后看双方位置后面是否与对方当前位置相等 如果相等 则直接判断后面是否为回文 否则直接为False
def validPalindrome(s: str) -> bool:
    if s == s[::-1]: return True
    i = 0
    j = len(s)-1
    while s[i] == s[j] and j>=i:
        i+=1
        j-=1
    if s[i] == s[j-1]:
        print(s[i:i+((j-i)//2)+1], s[j-1-((j-i)//2):j])
        if s[i:i+((j-i)//2)+1] == s[j-1-((j-i)//2):j][::-1]:
            return True
    if s[i+1] == s[j]:
        print(s[i+1:i+2+ ((j - i) // 2)], s[j - ((j - i) // 2):j+1])
        if s[i+1:i+2+ ((j - i) // 2)] == s[j - ((j - i) // 2):j+1][::-1]:
            return True
    return False


# a = "abac"
a = 'abcaba'
print(validPalindrome(a))