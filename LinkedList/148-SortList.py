# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        # merge sort
        # termination
        if not head or not head.next:
            return head
        # find mid with slow, fast
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # slow is mid
        right = slow.next
        slow.next = None  # cut off the right part
        left = head
        left = self.sortList(left)  # keep spliting left part
        right = self.sortList(right)  # keep spliting right part
        return self.merge(left, right)

    def merge(self, left, right):
        # merge two sorted list
        dummy = ListNode()
        # we don't want to change dummy during iteration
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
                curr = curr.next
            else:
                curr.next = right
                right = right.next
                curr = curr.next
        # rest of the nodes, directly link it
        if left:
            curr.next = left
        if right:
            curr.next = right
        return dummy.next
