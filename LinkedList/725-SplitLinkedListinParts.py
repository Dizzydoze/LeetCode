# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # get the length of linked list
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        # create a list to store k parts of linked list
        parts = [None] * k
        # get minimum part size(n) and number of extra nodes
        n, extra = length // k, length % k
        # KEY: the first 'extra' parts will have n + 1 nodes
        curr = head
        # for each part of the linked list, we traverse and find the cutting point
        i = 0
        while i < k and curr:
            # add current node to parts
            parts[i] = curr
            # traverse current part to find the cutting point
            # each part can only have 1 more node as required
            for _ in range(n + (1 if i < extra else 0) - 1):
                curr = curr.next
            # curr is now pointing at cutting point, cut it
            nxt = curr.next
            curr.next = None
            curr = nxt
            i += 1
            # we don't need to handle i, when i == extra, all extra nodes has been equally distributed to first 'extra' part.
        return parts
