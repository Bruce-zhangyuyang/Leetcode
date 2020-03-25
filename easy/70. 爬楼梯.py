def climbStairs(n: int) -> int:
    fst = 1
    scd = 2
    tol = 0
    for i in range(2, n):
        tol = fst + scd
        fst = scd
        scd = tol
    return max(tol, n)

n = 5
print(climbStairs(n))