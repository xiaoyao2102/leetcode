from datastructure import ListNode


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0

        while cur and count != k:
            cur = cur.next
            count += 1

        if count == k:
            cur = self.reverseKGroup(cur, k)

            while count > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur

        return head
