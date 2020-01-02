# # 思路：暴力解法
# # 执行用时 :140 ms, 在所有 Python3 提交中击败了21.69%的用户
# # 内存消耗 :12.6 MB, 在所有 Python3 提交中击败了98.87%的用户
# def repeatedSubstringPattern(s: str) -> bool:
#     for i in range(1, len(s)//2+1):
#         if s[:i]*(len(s)//i) ==s:
#             print(s[:i])
#             return True
#     return False

# 思路：借鉴网上思路，如果是有重复的，那么s一定是2s的子集
def repeatedSubstringPattern(s: str) -> bool:
    return s in (s + s)[1:-1]

# s = "abab"
# s = "aba"
s = "abcabcabcabc"
print(repeatedSubstringPattern(s))