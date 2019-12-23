def wordPattern(pattern: str, str: str) -> bool:
    dic = {}
    for index, str in enumerate(pattern):
        str = str(str) # 错误：'str' object is not callable
        if not dic[str]:
            dic[str] = [index]
        else:
            dic[str].append(index)
    dic_ = {}
    for a, b in enumerate(str.split()):
        if not dic[b]:
            dic_[b] = [a]
        else:
            dic_[b].append(a)
    print(dic_.values(), dic.values())
    return  dic_.values() == dic.values()


pattern = "abba"
str = "dog cat cat dog"
print(wordPattern(pattern, str))

