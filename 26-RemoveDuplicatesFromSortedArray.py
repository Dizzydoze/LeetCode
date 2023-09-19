class Solution:
    def removeDuplicates(self, nums):
        # special case
        if len(nums) < 2:
            return 1
        # two pointers,
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1
            right += 1
        return left + 1
