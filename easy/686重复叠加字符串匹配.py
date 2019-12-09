# def repeatedStringMatch(A: str, B: str) -> int:
#     num = len(B)//len(A)
#     for i in range(num, 20000):
#         C = A*i
#         if len(C)>10000:
#             return -1
#         if B in C: return i

def repeatedStringMatch(self, A: str, B: str) -> int:
    num = len(B)//len(A)
    C = A*num
    if B in C: return num
    if B in C+A: return num+1
    if B in C+A*2: return num+2
    else: return -1


A = "abcd"
B = "cdabcdab"
a = repeatedStringMatch(A, B)
print(a)