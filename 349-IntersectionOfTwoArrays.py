class Solution:
    def intersection(self, nums1, nums2):
        # two pointers, sort
        nums1.sort()
        nums2.sort()
        left, right = 0, 0
        res = []
        while left < len(nums1) and right < len(nums2):
            # left > right, move right
            if nums1[left] > nums2[right]:
                right += 1
            # left < right, move left
            elif nums1[left] < nums2[right]:
                left += 1
            else: # left == right, move both
                res.append(nums1[left])
                left += 1
                right += 1
        return set(res)
