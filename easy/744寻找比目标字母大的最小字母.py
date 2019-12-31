from typing import  List
# 执行用时 :132 ms, 在所有 python3 提交中击败了 71.32%的用户
# 内存消耗 :12.9 MB, 在所有 python3 提交中击败了100.00%的用户
# 思路：循环26个字母 找到比目标字母大的最小字母
def nextGreatestLetter(letters: List[str], target: str) -> str:
    x = ord(target) + 1
    while x != ord(target):
        if x > 122:
            x = 97
        if chr(x) in letters:
            return chr(x)
        else:
            x += 1

letters = ["c", "f", "j"]
target = "c"
print(nextGreatestLetter(letters, target))