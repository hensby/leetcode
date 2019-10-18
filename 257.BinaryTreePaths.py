# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res, path= [], ''
        if not root:return []
        else:self.binaryTreePathsHelper(root, res, '')
        return res

    def binaryTreePathsHelper(self, root:TreeNode, res:List, path:str):
        if root.left is None and root.right is None:
            res.append(path + str(root.val))
            return
        if root.left: self.binaryTreePathsHelper(root.left, res, path+str(root.val)+'->')
        if root.right: self.binaryTreePathsHelper(root.right, res, path+str(root.val)+'->')
