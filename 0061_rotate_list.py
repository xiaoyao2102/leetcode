from datastructure import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        list_len = 1
        tail = head
        while tail.next:
            list_len += 1
            tail = tail.next

        tail.next = head

        k %= list_len

        if k:
            for i in range(list_len - k):
                tail = tail.next
        new_head = tail.next
        tail.next = None

        return new_head
