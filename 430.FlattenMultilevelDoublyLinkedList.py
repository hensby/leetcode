
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        node = head
        while node:
            node_next = node.next
            if node.child:
                flattened = self.flatten(node.child)
                node.child = None
                nextNode = self.appendToList(node, flattened)
                node = nextNode
            else:
                node = node.next
        return head

    def appendToList(self, node, listToAppendHead):
        next_node = node.next
        node.next = listToAppendHead
        listToAppendHead.prev = node
        while node.next:
            node = node.next
        node.next = next_node
        if next_node:
            next_node.prev = node
        return next_node

# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         if head == None:return None
#         if head.next ==None and head.child == None :return head
#         self.flattenHelper(head)
#         return head
#
#     def flattenHelper(self, head: 'Node'):
#         if head.next==None and head.child==None:return head
#         cur = head
#         # nxt = head.next
#         if cur.child:
#             cur.next = cur.child
#             cur = cur.child
#             self.flattenHelper(cur)
#
#         while cur and cur.next:

