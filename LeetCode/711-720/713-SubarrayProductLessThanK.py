class Solution:
    """sliding window"""
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # original product before start
        res, left, product = 0, 0, 1
        for right in range(len(nums)):
            product *= nums[right]
            # product too big, divide previous elements
            # left == right, window has 1 element
            while product >= k and left <= right:
                # keep divide previous numbers until product < k
                product /= nums[left]
                left += 1
            # KEY: number of subarrays, previous subarrays are excluded
            res += right - left + 1
        return res
