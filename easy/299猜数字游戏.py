# # 理解错误 直接把位置输出
# def getHint(secret: str, guess: str) -> str:
#     x = ''
#     p, q = {}, []
#     for i in range(len(secret)):
#         if secret[i] == guess[i]:
#             x += f'{i+1}A'
#         else:
#             if secret[i] not in p:
#                 p[secret[i]] = [i]
#             else:
#                 p[secret[i]].append(i)
#             q.append(guess[i])
#     for i in p:
#         if i in q:
#             x += f'{p[i].pop(0)+1}B'
#             q.remove(i)
#     return x


# 执行用时 :52 ms, 在所有 Python3 提交中击败了58.89%的用户
# 内存消耗 :13.1 MB, 在所有 Python3 提交中击败了77.14%的用户
def getHint(secret: str, guess: str) -> str:
    x = ''
    p, q = [], []
    y = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            y +=1
        else:
            p.append(secret[i])
            q.append(guess[i])
    x += f'{y}A'
    y = 0
    r, t = 0, 0
    p = sorted(p)
    q = sorted(q)
    while r < len(p) and t < len(q):
        if p[r] == q[t]:
            y += 1
            t += 1
            r += 1
        elif p[r] > q[t]:
            t += 1
        elif p[r] < q[t]:
            r += 1

    x += f'{y}B'
    return x

secret = "1807"
guess = "7810"

# secret = "1123"
# guess = "0111"
print(getHint(secret, guess))