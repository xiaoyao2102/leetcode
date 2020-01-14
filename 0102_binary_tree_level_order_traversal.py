from datastructure import TreeNode
from typing import List
from collections import deque


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []

        self._search(root, 0, result)

        return result

    def _search(self, node, level, result):
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

assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]
