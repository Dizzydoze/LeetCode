# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # dummy head
        dummy = ListNode()
        cur = dummy
        a, b = list1, list2
        # traverse both first
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        # there will still be one longer
        while a:
            cur.next = a
            cur = cur.next
            a = a.next
        while b:
            cur.next = b
            cur = cur.next
            b = b.next
        return dummy.next
