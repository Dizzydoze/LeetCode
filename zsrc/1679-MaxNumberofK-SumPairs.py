class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # two pointers, sorting
        nums.sort()
        res, l, r = 0, 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s > k:    # too big, r should be smaller
                r -= 1
            elif s < k:  # too small, l should be larger
                l += 1
            else:        # match found, both pointer get closer
                res += 1
                l += 1
                r -= 1
        return res
