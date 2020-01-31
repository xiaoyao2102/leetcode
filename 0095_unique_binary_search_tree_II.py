from typing import List

from datastructure import TreeNode


class Solution:

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self._generate_trees(1, n)

    def _generate_trees(self, start_inclusive: int, end_inclusive: int) -> List[TreeNode]:
        if start_inclusive > end_inclusive:
            return [None]

        if start_inclusive == end_inclusive:
            return [TreeNode(start_inclusive)]

        result = []

        for i in range(start_inclusive, end_inclusive + 1):

            left_trees = self._generate_trees(start_inclusive, i - 1)
            right_trees = self._generate_trees(i + 1, end_inclusive)

            for lt in left_trees:
                for rt in right_trees:
                    result.append(self._create_tree_node(i, lt, rt))

        return result

    def _create_tree_node(self, value: int, left: TreeNode, right: TreeNode) -> TreeNode:
        t = TreeNode(value)
        t.left = left
        t.right = right
        return t


solution = Solution()

assert len(solution.generateTrees(3)) == 5
assert len(solution.generateTrees(2)) == 2
assert len(solution.generateTrees(1)) == 1
assert len(solution.generateTrees(4)) == 14
