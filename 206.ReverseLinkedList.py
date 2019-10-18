# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:return None
        cur = head
        nxt = head.next
        pre = None
        while nxt:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next
        cur.next = pre
        return cur
