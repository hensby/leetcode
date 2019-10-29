# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        head1, head2 = headA, headB
        while head1 != head2:
            head1 = head1.next if head1 else headB
            head2 = head2.next if head2 else headA
        return head1