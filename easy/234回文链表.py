# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 思路：把链表上的值存到列表中 然后用列表进行比较

class Solution:
    def isPalindrome(head: ListNode) -> bool:
        if not head : return True
        a = []
        a.append(head.val)
        while head.next:
            head = head.next
            a.append(head.val)
        if a == a[::-1]:
            return True
        else:
            return False