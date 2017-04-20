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
    def doSort(self, head, end):

        split = head.next
        previous = split
        
        if head.next == end:
            return

        if split:
            current = split.next

            while current and current != end.next:
                if current:
                    if current.val < split.val:
                        previous.next = current.next
                        current.next = head.next
                        head.next = current
                    else:
                        previous = previous.next
                
                if previous:
                    current = previous.next

            self.doSort(head, split)
            self.doSort(split, end)

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummyHead = ListNode(None)
        dummyHead.next = head
        
        if not head:
            return None

        end = dummyHead

        while end.next:
            end = end.next

        self.doSort(dummyHead, end)

        return dummyHead.next

if __name__ == "__main__":
    input = [3,3,1,3,1,3,3,2,3,2,2,1,1,1,3,2,2,1,1,2,2,2,3,3,1,1,2,2,2,1,2,1,1,2,3,3,2,2,3,2,3,2,2]

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