# Definition for a binary tree node.
import binaryTree as bt
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 一个在左子树，一个在右子树
            return root
        elif left:  # 都在左子树
            return left
        elif right:  # 都在右子树
            return right
        else:
            return


    # 查找，分别在root的左右子树则为最近根节点。此方法超时
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if p.val > q.val:
    #         tmp = p
    #         p = q
    #         q = tmp
    #     if self.findInTree(root.left, p) and self.findInTree(root.left, q):
    #         return self.lowestCommonAncestor(root.left,p,q)
    #     elif self.findInTree(root.right, p) and self.findInTree(root.right, q):
    #         return self.lowestCommonAncestor(root.right,p,q)
    #     else: return root
    #
    #
    # def findInTree(self, root:'TreeNode', son: 'TreeNode'):
    #     if root==None:return False
    #     if root.val==son.val:return True
    #     elif self.findInTree(root.left, son) or self.findInTree(root.right, son):
    #         return True


if __name__ == '__main__':
    t = bt.Tree()
    for i in range(10):
        t.add(i)
