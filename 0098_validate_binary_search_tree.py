from datastructure import TreeNode


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        return self._is_valid(root)

    def _is_valid(self, node: TreeNode, low_limit=float('-inf'), high_limit=float('inf')) -> bool:
        if not node:
            return True

        if node.val <= low_limit or node.val >= high_limit:
            return False

        return self._is_valid(node.left, low_limit, node.val) and self._is_valid(node.right, node.val, high_limit)


solution = Solution()
t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)
assert solution.isValidBST(t)

t = TreeNode(5)
t.left = TreeNode(1)
t.right = TreeNode(4)
t.right.left = TreeNode(3)
t.right.right = TreeNode(6)
assert not solution.isValidBST(t)