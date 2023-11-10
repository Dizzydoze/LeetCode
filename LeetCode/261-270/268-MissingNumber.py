class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # loop
        n = len(nums)
        for i in range(n + 1):
            if n - i not in nums:
                return n - i


class Solution2:
    """Faster, math"""
    def missingNumber(self, nums: List[int]) -> int:
        # math, difference is the missing one
        # missing num = sum([0, n]) - sum(num in array)
        return sum(range(len(nums)+1)) - sum(nums)