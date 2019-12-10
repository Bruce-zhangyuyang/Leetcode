# 思路：如果两个长度不一样 直接返回false
#       如果两个相同，则看单个里面是否有重复字符
#       如果两个不相同就看不一样的地方是不是只有两个 并且两个正好顺序颠倒
def buddyStrings(A: str, B: str) -> bool:
    if len(A)!=len(B): return False
    if A == B:
        set_ = []
        for a in A:
            if a in set_:
                return True
            set_.append(a)
        return False
    else:
        dif = []
        for i in zip(A, B):
            if i[0]!=i[1]:
                dif.append(i)
        if len(dif)>=3 or len(dif) == 1: return False
        else:
            if len(dif) ==2 and dif[0] == dif[1][::-1]:
                return True

A = "aaaaaaabc"
B = "aaaaaaacb"
s = buddyStrings(A, B)
print(s)





