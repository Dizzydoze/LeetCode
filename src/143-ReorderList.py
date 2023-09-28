# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # save all nodes into array
        arr = list()
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        # two pointers
        left, right = 0, len(arr) - 1

        while left < right:
            # step1: point left to right
            arr[left].next = arr[right]
            # move left forward
            left += 1
            # KEYPOINT: reach the last node, break
            if left == right:
                break
            # step2: point right to current left
            arr[right].next = arr[left]
            # move right backward
            right -= 1
            # step3: disconnect current right
            arr[right].next = None
