class Solution:
    """Sorting"""
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        # SHOULD BE QUICK SORT, BUCKET SORT, INSERTION SORT, etc.
        nums.sort()
        max_diff = float('-inf')
        for i in range(1, len(nums)):
            max_diff = max(max_diff, nums[i] - nums[i - 1])
        return max_diff
