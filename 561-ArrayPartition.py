class Solution:
    def arrayPairSum(self, nums) -> int:
        # Greedy, Sort
        # Sort and every time largest num added
        nums.sort()
        right = len(nums) - 1
        minn = 0
        res = 0
        while right >= 1:
            minn = nums[right - 1]  # left one must be smaller
            res += minn
            right -= 2
        return res
