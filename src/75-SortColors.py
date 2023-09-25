class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting
        red = nums.count(0)
        white = nums.count(1)
        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif red <= i < white + red:
                nums[i] = 1
            else:
                nums[i] = 2


class Solution2:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers
        n = len(nums)
        l, curr, r = 0, 0, n - 1
        while curr <= r:
            if nums[curr] == 0:  # 0, move to the left side
                nums[l], nums[curr] = nums[curr], nums[l]
                curr += 1
                l += 1
            elif nums[curr] == 2:  # 2, move to the right side
                nums[curr], nums[r] = nums[r], nums[curr]
                # still confused why we don't move curr forward???
                r -= 1
            else:  # 1, we skip, move curr forward
                curr += 1
