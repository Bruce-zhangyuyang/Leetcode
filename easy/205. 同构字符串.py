# 执行用时 :140 ms, 在所有 Python3 提交中击败了5.56%的用户
# 内存消耗 :28.8 MB, 在所有 Python3 提交中击败了5.08%的用户
# 思路： 如果两个都没有 就分别增加到字典和集合里面， 要是其中一个有， 只要另外一个不对应 就返回False
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    used = {}
    C_ = []
    for a, q in zip(s, t):
        if a not in used and q not in C_:
            used[a] = q
            C_.append(q)
        elif a not in used:
            return False
        elif q != used[a]:
            return False
    return True

s = "aa"
t = "ab"
print(isIsomorphic(s, t))
