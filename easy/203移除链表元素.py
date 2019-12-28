# 执行用时 :68 ms, 在所有 python3 提交中击败了93.92%的用户
# 内存消耗 :15.6 MB, 在所有 python3 提交中击败了98.79%的用户
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        s = ListNode(0)
        s.next =  head
        he = s
        while he.next != None:
            if he.next.val == val:
                he.next = he.next.next
            else:
                he = he.next
        return s.next