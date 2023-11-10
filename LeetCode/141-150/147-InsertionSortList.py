# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    draw to see how prev, last_sorted and curr moving and how they disconnect, reconnect.
    """
    def insertionSortList(self, head):
        # insertion sort, n^2 complexity
        dummy = ListNode()
        dummy.next = head
        last_sorted = head
        curr = head.next

        while curr:
            # no need for insertion
            if last_sorted.val <= curr.val:
                last_sorted = last_sorted.next
            # ready to insert the curr.val before last_sorted
            else:
                # KEY POINT: prev.next is the spot where the curr should insert
                prev = dummy
                # keep moving prev forward, until prev.next is the insertion spot
                while prev.next.val <= curr.val:
                    prev = prev.next
                # found the insertion spot for curr, start the switch
                # first remove the curr node from last_sorted
                last_sorted.next = curr.next
                # then insert the curr
                curr.next = prev.next
                # finally reconnect the prev node
                prev.next = curr
            # curr and last_sorted switch the places, curr should always next to last_sorted
            curr = last_sorted.next
        return dummy.next
