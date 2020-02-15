from datastructure import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


l = ListNode(0)
l.next = ListNode(1)
l.next.next = ListNode(2)

solution = Solution()
new_l = solution.reverseList(l)

assert new_l.val == 2
assert new_l.next.val == 1
assert new_l.next.next.val == 0

