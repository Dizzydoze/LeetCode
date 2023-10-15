# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """decimal calculation"""
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        extra = 0
        # mind the last extra should still be added
        while l1 or l2 or extra:
            sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + extra
            # current spot value
            node = ListNode(sum_ % 10)
            # next spot value
            extra = sum_ // 10
            cur.next = node
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
