class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertBinaryTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None

        # swap its children
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursively invert child trees and return
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
        return root
