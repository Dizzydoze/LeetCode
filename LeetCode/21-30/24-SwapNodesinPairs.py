# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        prev, cur, res = None, head, head.next
        while cur and cur.next:
            # switch two nodes
            nxt = cur.next
            # if there's a prev node, connect it to the new re-ordered node first
            if prev:
                prev.next = nxt
            cur.next = nxt.next
            nxt.next = cur
            # KEY: use prev to store previous cur node
            prev = cur
            # move cur to first node of the next pair
            cur = cur.next
        # because head might switch place with head.next, either of them could be ans
        return res or head
