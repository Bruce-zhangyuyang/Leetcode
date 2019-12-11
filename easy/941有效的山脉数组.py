from typing import List
# 思路：找到临界山顶 然后没有相等的存在的降序 输出为True

def validMountainArray(A: List[int]) -> bool:
    if len(A) < 3: return False
    a = 0
    while a < len(A)-1 and A[a] < A[a+1] :
        a += 1
    if a == 0: return False
    s = A[a:]
    s_ = sorted(s)[::-1]
    print(s, s_)
    if s == s_ and len(set(s_)) > 1 and len(set(s_)) == len(s_): return True
    else: return False


# A = [2,1]
# A = [3,5,5]
# A =[0,3,2,1]
# A = [0,1,2,3,4,5,6,7,8,9]
A = [14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]
print(validMountainArray(A))