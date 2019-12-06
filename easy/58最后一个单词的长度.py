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

def lengthOfLastWord(s: str) -> int:
    return len(s.rstrip().split(" ")[-1])


s= ""
a = lengthOfLastWord(s)
print(a)