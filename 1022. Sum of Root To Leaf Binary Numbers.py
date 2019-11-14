# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        tmp= [root.val]
        r = 0
        if not root.right and not root.left:
            return root.val
        if root.left:
            self.dsf(root.left, res, tmp.copy())
        if root.right:
            self.dsf(root.right, res, tmp.copy())
        for i in res:
            for j in range(len(i)):
                r += i[j]*2**(len(i)-j-1)
        return r

    def dsf(self,root: TreeNode, res, tmp)->int:
        if not root.right and not root.left:
            tmp.append(root.val)
            res.append(tmp)
        if root.left or root.right:
            s = root.val
            tmp.append(root.val)
            if root.right:
                self.dsf(root.right, res, tmp.copy())
            if root.left:
                self.dsf(root.left, res, tmp.copy())