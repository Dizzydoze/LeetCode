# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        # length difference for longer one to move in advance
        a_len, b_len = 0, 0
        a, b = headA, headB
        while a:
            a_len += 1
            a = a.next
        while b:
            b_len += 1
            b = b.next
        diff = abs(a_len - b_len)
        # longer list move in advance
        while diff:
            if a_len > b_len:
                headA = headA.next
            else:
                headB = headB.next
            diff -=1
        # now start at the same point
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
