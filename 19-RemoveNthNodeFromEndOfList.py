# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        # Two pointers
        dummy = ListNode(0, head)
        # slow pointer starts one step slower
        slow = dummy
        fast = head
        # fast move n steps first
        for _ in range(n):
            fast = fast.next
        # move together until fast pointer reach None
        while fast:
            slow = slow.next
            fast = fast.next
        # now slow the node needed to be relinked
        slow.next = slow.next.next
        return dummy.next