from datastructure import TreeNode
from typing import List


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []

        self._search(root, 0, result)

        for i in range(len(result)):
            if i % 2 == 1:
                result[i] = result[i][::-1]

        return result

    def _search(self, node: TreeNode, level: int, result: List[List[int]]):
        if level >= len(result):
            result.append([node.val])
        else:
            result[level].append(node.val)

        if node.left:
            self._search(node.left, level + 1, result)
        if node.right:
            self._search(node.right, level + 1, result)


solution = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
assert solution.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
assert solution.zigzagLevelOrder(root) == [[3], [20, 9], [2, 4, 15, 7]]
