# 执行用时 :24 ms, 在所有 python3 提交中击败了98.86%的用户
# 内存消耗 :12.6 MB, 在所有 python3 提交中击败了100.00%的用户
# 思路：建立两个字典 然后比较两个字典的值
def wordPattern(pattern: str, str: str) -> bool:
    dic = {}
    pat = [p for p in pattern]
    for index, st in enumerate(pat):
        if st not in dic:
            dic[st] = [index]
        else:
            dic[st].append(index)
    x = str.split()
    dic_ = {}
    for ind, b in enumerate(x):
        if b not in dic_:
            dic_[b] = [ind]
        else:
            dic_[b].append(ind)
    print(sorted(dic_.values()), sorted(dic.values()))
    return  sorted(dic_.values()) == sorted(dic.values())


pattern = "abba"
str = "dog cat cat dog"
# pattern = "aaaa"
# str = "dog cat cat dog"
print(wordPattern(pattern, str))

