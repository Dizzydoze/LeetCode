# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        # slow, fast two pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next       # one step
            fast = fast.next.next  # two steps
        return slow                # slow is right at mid when fast reach the end
