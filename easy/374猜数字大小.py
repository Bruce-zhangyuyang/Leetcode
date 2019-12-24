# 思路：二分法进行查找
def guessNumber(self, n: int) -> int:
    start = 1
    end = n + 1
    while guess((start + end)//2) !=0:
        if guess((start + end)//2) == -1:
            end = (start + end)//2
        else:
            start = (start + end)//2
    return (start + end)//2

n = 10, pick = 6