# Definition for a binary tree node.
import binaryTree as bt
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None: return None
        if p.val > q.val:
            tmp = p
            p = q
            q = tmp
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

# if __name__ == '__main__':
#     so = Solution()
#     t = bt.Tree()
#     tree = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
#     for i in tree:
#         t.add(i)
#     print(so.lowestCommonAncestor(t.root, 2, 8))