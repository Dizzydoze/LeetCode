class Solution:
    def sortArrayByParity(self, nums):
        # two pointers
        left = 0
        # find the first odd
        while left < len(nums):
            if nums[left] % 2 != 0:
                break
            left += 1
        right = left + 1
        while right < len(nums):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1
        return nums
