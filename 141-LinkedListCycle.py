# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        # Special cases
        if not head or not head.next:
            return False
        # Fast and Slow Two Pointers, Floyd Loop
        slow = head
        fast = head.next
        # loop condition: slow != fast
        while slow != fast:
            # cycle not exist
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
