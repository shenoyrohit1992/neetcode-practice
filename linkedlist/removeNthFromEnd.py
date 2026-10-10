class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

    def removeFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0, head)
        slow, fast = dummy, head
        # start slow one before fast, we end one-before elem to skip

        # offset s-f by exactly n
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        # set slow's next to skip one node
        slow.next = slow.next.next
        return dummy.next
