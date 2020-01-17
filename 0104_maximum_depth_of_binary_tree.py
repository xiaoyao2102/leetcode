from datastructure import TreeNode


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left:
            return self.maxDepth(root.right) + 1

        if not root.right:
            return self.maxDepth(root.left) + 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


solution = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
assert solution.maxDepth(root) == 3

root = TreeNode(3)
assert solution.maxDepth(root) == 1

root = TreeNode(3)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
assert solution.maxDepth(root) == 3
