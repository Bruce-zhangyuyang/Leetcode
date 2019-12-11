# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 思路： 二分法找第一个True


def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    start = 1
    end = n
    while(end>start):
        mid = (start + end)//2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    return end