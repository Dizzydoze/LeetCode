class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        nums.sort()  # sort
        diff, left =  10**5, 0   # sliding window, width = k
        while (left + k - 1) < len(nums):  # left + k slice
            cur_diff = nums[left+k-1] - nums[left]
            if cur_diff < diff:  # update if smaller diff
                diff = cur_diff
            left += 1  # move the window forward
        return diff
