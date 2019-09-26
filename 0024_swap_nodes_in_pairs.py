from datastructure import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)

        pre.next = head

        while pre.next and pre.next.next:
            current = pre.next
            current_next = pre.next.next

            pre.next, current.next, current_next.next = current_next, current_next.next, current
            pre = current
        return dummy.next
