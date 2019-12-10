# 思路1：如果如果为空或者只有空格 则返回0
#        如果没有空格 并且有单词 就返回单词长度
#        不然就分词， 然后把非空的放进q中， 然后返回q中最后一个单词长度

# def lengthOfLastWord(s: str) -> int:
#     if len(s) == 0 or (len(s) == 1 and s.find(' ') == 0): return 0
#     if s.find(' ') == -1 and len(s) >= 1: return len(s)
#     p = s.split(' ')
#     q = []
#     for i in p:
#         if i != '':
#             q.append(i)
#     if q:
#         return len(q[-1])
#     else:
#         return 0

# 思路2： 直接删除最后的空格 然后分词 去最后一位单词长度


def lengthOfLastWord(s: str) -> int:
    return len(s.rstrip().split(" ")[-1])


s= ""
a = lengthOfLastWord(s)
print(a)