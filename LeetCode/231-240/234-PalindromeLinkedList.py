# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # nodes <= 1 should be palindrome
        if not head or not head.next:
            return True
        # 3 steps
        # 1. slow fast pointer finding the middle node
        # start at the same idx, slow is mid while fast reach the end
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2. reverse the second half of the linked list
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # 3. compare first and second list (value)
        h, p = head, prev
        # PS: all nodes are still connected in head node, we should use prev to loop
        while p:
            if h.val != p.val:
                return False
            h = h.next
            p = p.next
        return True
