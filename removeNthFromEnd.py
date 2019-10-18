# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # count = 0
        # tmp = ListNode(0)
        # tmp.next = head
        # first = tmp.next
        # while first:
        #     count += 1
        #     first = first.next
        # count=count-n
        # first = tmp
        # while count>0:
        #     count-=1
        #     first = first.next
        # first.next = first.next.next
        # return tmp.next
        tmp = ListNode(0)
        tmp.next = head
        first = second = tmp.next
        for i in range (n):
            first = first.next
        while first.next and second.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return tmp.next
