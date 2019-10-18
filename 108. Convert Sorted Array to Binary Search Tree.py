# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        target = len(nums) // 2
        root = TreeNode(nums[target])
        root.left = self.sortedArrayToBST(nums[: target])
        root.right = self.sortedArrayToBST(nums[target + 1:])
        return root


