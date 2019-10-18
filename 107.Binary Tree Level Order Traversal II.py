# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        queue = []
        cur = [root]
        while cur:
            nestNode = []
            curNodeValue = []
            for i in cur:
                curNodeValue.append(i.val)
                if i.left:
                    nestNode.append(i.left)
                if i.right:
                    nestNode.append(i.right)
            queue.insert(0, curNodeValue)
            cur = nestNode
        return queue
