class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == 0:
                if nums[right] != 0:  # switch while left == 0, right != 0
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
                else:
                    right += 1  # move right until non-zero is found
            else:   # move both until left find zero, right find non-zero
                left += 1
                right += 1
