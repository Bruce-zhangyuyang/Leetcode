# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 思路：分成4种情况 要是空的 直接返回0 要是只有左（右）子节点，则继续执行左（右）子节点，要是都有，则返回两边的最小值
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        # def count(node):
        #     if not node:
        #         return 0
        #     else:
        #         rleft = count(node.left)
        #         rright = count(node.right)
        #         x = min(rleft, rright) +1
        #         return x

        if not root:
            return 0
        elif not root.right:
            return self.minDepth(root.left) + 1
        elif not root.left:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1






