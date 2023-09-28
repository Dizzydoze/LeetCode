class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window
        n = len(nums)
        # start from adding first num in the list
        # longest length can never exceed len(nums) + 1
        l, r, minilen = 0, 0, n + 1
        s = 0
        while r < n:
            s += nums[r]
            # keep moving left forward if greater
            while s >= target:
                minilen = min(minilen, r - l + 1)
                s -= nums[l]
                l += 1
            # keep moving right forward if we don't reach the target
            r += 1
        # there's no minilen if even the whole list len(nums) does not match
        return 0 if minilen == n + 1 else minilen
