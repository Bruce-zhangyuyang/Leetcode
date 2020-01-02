# 思路：每个字符串一个指针
# 执行用时 :24 ms, 在所有 Python3 提交中击败了99.62%的用户
# 内存消耗 :12.8 MB, 在所有 Python3 提交中击败了100.00%的用户
def isLongPressedName(name: str, typed: str) -> bool:
    j = 0
    for i in range(len(typed)):
        print(j)
        if j<len(name) and typed[i] == name[j]:
            j += 1
        elif j!=0 and typed[i] == name[j-1]:
            continue
        else: return False
    if len(name)> j:
        return False
    else:
        return True

name = "pyplrz"


typed = "ppyypllr"
print(isLongPressedName(name, typed))