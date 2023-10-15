class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # two pointers start from both side
        # left for storing, right for replacing
        left, right = 0, len(nums) - 1
        while left <= right:
            # replace left with right until left is no more target
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                # left is no more target, move forward
                left += 1
        return left
