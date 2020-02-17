from typing import List
# 思路:从后往前遍历pop
def checkIfExist(arr: List[int]) -> bool:
    len_ = len(arr)
    for i in range(len_)[::-1]:
        x = arr.pop(i)
        if x*2 in arr or x/2 in arr:

            return True
        else:
            arr = arr[:i]
    return False


# arr = [10,2,5,3]
# arr = [3, 1, 7, 11]
arr = [-2,0,10,-19,4,6,-8]
print(checkIfExist(arr))