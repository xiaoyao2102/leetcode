from datastructure import TreeNode


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


solution = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
assert solution.minDepth(root) == 2

root = TreeNode(3)
assert solution.minDepth(root) == 1

root = TreeNode(3)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
assert solution.minDepth(root) == 3
