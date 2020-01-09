from datastructure import TreeNode


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self._search_p_or_q(root, p, q)

    def _search_p_or_q(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self._search_p_or_q(root.left, p, q)
        right = self._search_p_or_q(root.right, p, q)

        return root if (left and right) else (left or right)


solution = Solution()

r = TreeNode(3)
r.left = TreeNode(5)
r.right = TreeNode(1)
r.left.left = TreeNode(6)
r.left.right = TreeNode(2)
r.right.left = TreeNode(0)
r.right.right = TreeNode(8)
r.left.right.left = TreeNode(7)
r.left.right.right = TreeNode(4)

assert solution.lowestCommonAncestor(r, TreeNode(5), TreeNode(1)).val == 3
assert solution.lowestCommonAncestor(r, TreeNode(7), TreeNode(4)).val == 2
