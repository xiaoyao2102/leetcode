from datastructure import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        list_len = 1
        tail = head
        # find the last node
        while tail.next:
            list_len += 1
            tail = tail.next

        # make list to a ring
        tail.next = head

        k %= list_len

        # find the new header and break the ring
        if k:
            for i in range(list_len - k):
                tail = tail.next
        new_head = tail.next
        tail.next = None

        return new_head
