class Solution:
    def findLHS(self, nums) -> int:
        # sort first
        nums.sort()
        max_len, left = 0, 0
        # two pointers, sliding window
        for right in range(len(nums)):  # use for loop auto update right pointer
            if nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:  # perfect match, update maxlen
                max_len = max(max_len, right - left + 1)
        return max_len
