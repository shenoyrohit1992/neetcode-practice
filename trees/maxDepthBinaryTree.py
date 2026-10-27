import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def findDepthOfNode(node):
            if not node:
                return 0

            return 1 + max(findDepthOfNode(node.left), findDepthOfNode(node.right))

        return findDepthOfNode(root)

    def maxDepthBFS(self, root: TreeNode) -> int:
        # Level order traversal of tree
        if not root:
            return 0

        level = 0
        q = collections.deque([root])

        while q:
            # snapshot of every level one at a time
            for _ in range(len(q)):
                # pop one at a time, if they have children, append to q (for next level)
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
