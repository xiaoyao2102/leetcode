from typing import List

from datastructure import ListNode


class SolutionOne:

    """
    Compared one by one
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = dummy = ListNode(0)

        while True:
            min_val = 2147483647
            min_index = None
            to_break = True
            for index in range(len(lists)):
                if lists[index]:
                    if lists[index].val < min_val:
                        min_index = index
                        min_val = lists[index].val
                    to_break = False

            if to_break:
                break

            dummy.next = lists[min_index]
            dummy = dummy.next

            lists[min_index] = lists[min_index].next
        return head.next


class SolutionTwo:

    """
    Priority Queue
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        head = dummy = ListNode(0)

        count = 0

        q = PriorityQueue()

        for i in range(len(lists)):
            temp = lists[i]
            while temp:
                q.put((temp.val, count, temp))
                temp = temp.next
                count += 1

        while not q.empty():
            dummy.next = q.get()[2]
            dummy = dummy.next

        return head.next


class SolutionThree:

    """
    Merge list one by one
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1:
                return l2

            if not l2:
                return l1

            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1, l2.next)
                return l2

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval << 1):
                print(i, amount, interval)
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval = interval << 1
        return lists[0] if amount > 0 else lists


class SolutionFour:

    """
    Sorted directly
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodes = []
        for l in lists:
            while l:
                nodes.append(l)
                l = l.next
        nodes = sorted(nodes, key=lambda x: x.val)
        dummy = head = ListNode(0)
        for node in nodes:
            head.next = node
            head = head.next
        return dummy.next
