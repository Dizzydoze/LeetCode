class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # three pointers, one for storage, two for iteration
        # all started from the last idx, moving backward
        k, left, right = m + n - 1, m - 1, n - 1
        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[k] = nums1[left]
                left -= 1
            else:  # nums2 is bigger, or no more nums in nums1
                nums1[k] = nums2[right]
                right -= 1
            k -= 1