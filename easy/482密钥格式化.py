# 思路：第一个不动，后面的按照K个一组进行分组 但是后面有可能不能满足K个 思路错误！！
# def licenseKeyFormatting(S: str, K: int) -> str:
#     S = S.upper()
#     t = S.find('-')
#     til = S[:t + 1]
#     til_ = S[t+1 :]
#     til_ = til_.replace('-', '')
#     print(til_)
#     w = 0
#     for i in range(len(til_)):
#         if i%K == K - 1 :
#             til = til+til_[w:i+1]+'-'
#             w = i+1
#     if len(til_)%K != 0:
#         til = til + til_[len(til_)%K+1:] +'-'
#
#     return til[:-1]


# 思路2：逆序添加- 来进行分组，第一个最少有一个元素
def licenseKeyFormatting(S: str, K: int) -> str:
    S = S.upper().replace('-', '')[::-1]
    til_ = ''
    for i in range(len(S)):
        til = S[i]
        if i % K == 0 and i!=0:
            til = '-' + S[i]
        til_ = til_ + til

    return til_[::-1]



S = "5F3Z-2e-9-w"
K = 4
# S = '2-5g-3j'
# K = 2
# S = "2-4A0r7-4k"
# K = 4
print(licenseKeyFormatting(S, K))