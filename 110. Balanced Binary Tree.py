# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 遍历每一节点的左右子树的高度，判定其是否符合条件；
    # 只要发现其不符合，立即退出，判定其不是平衡二叉树
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        # 分别定义左右子树的高度
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = self.get_depth(root.left)
        if root.right:
            right_depth = self.get_depth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    # 获取某一节点对应树的最大高度
    def get_depth(self, root):
        if root is None:
            return 0
        else:
            return max(self.get_depth(root.left), self.get_depth(root.right))+1

