from datastructure import TreeNode


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


solution = Solution()

r = TreeNode(6)
r.left = TreeNode(2)
r.right = TreeNode(8)
r.left.left = TreeNode(0)
r.left.right = TreeNode(4)
r.right.left = TreeNode(7)
r.right.right = TreeNode(9)
r.left.right.left = TreeNode(3)
r.left.right.right = TreeNode(5)

assert solution.lowestCommonAncestor(r, TreeNode(8), TreeNode(4)).val == 6
assert solution.lowestCommonAncestor(r, TreeNode(8), TreeNode(2)).val == 6
assert solution.lowestCommonAncestor(r, TreeNode(0), TreeNode(5)).val == 2
assert solution.lowestCommonAncestor(r, TreeNode(3), TreeNode(5)).val == 4
