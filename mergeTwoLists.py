# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = ListNode(0)
        result = s
        while l1 and l2:
            if l1.val<=l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
        if l1:
            while l1:
                result.next = l1
        if l2:
            while l2:
                result.next = l2
        return result.next