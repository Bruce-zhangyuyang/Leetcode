# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 执行用时 :372 ms, 在所有 python3 提交中击败了7.28%的用户
# 内存消耗 :13.4 MB, 在所有 python3 提交中击败了98.78%的用户

class Solution:
    def isSame(self, j, k):
        if not j and not k:
            return True
        if not j or not k:
            return False
        return (j.val == k.val) and self.isSame(j.left, k.left) and self.isSame(j.right, k.right)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# 思路：

# 执行用时 :244 ms, 在所有 python3 提交中击败了59.39%的用户
# 内存消耗 :13.9 MB, 在所有 python3 提交中击败了86.59%的用户

# class Solution:
#
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         def isSame(j, k):
#             if not j and not k:
#                 return True
#             if not j or not k:
#                 return False
#             return (j.val == k.val) and isSame(j.left, k.left) and isSame(j.right, k.right)
#
#         if not s:
#             return False
#         return isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)