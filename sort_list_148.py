# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self, part1, part2):
        dummyHead = ListNode(None)
        tail = dummyHead

        while part1 and part2:
            if part1.val <= part2.val:
                tail.next = part1
                tail = tail.next
                part1 = part1.next
            else:
                tail.next = part2
                tail = tail.next
                part2 = part2.next

        if part1:
            tail.next = part1
        else:
            tail.next = part2

        return dummyHead.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next

            if fast.next:
                fast = fast.next
                slow = slow.next


        part2 = slow.next
        slow.next = None

        first = self.sortList(head)
        second = self.sortList(part2)

        mergedHead = self.merge(first, second)
        return mergedHead

if __name__ == "__main__":
    input = [2]

    head = ListNode(1)
    current = head

    for item in input:
        newNode = ListNode(item)
        current.next = newNode
        current = current.next

    solution = Solution()
    solution.sortList(head)

    current = head

    while current:
        print current.val,
        current = current.next