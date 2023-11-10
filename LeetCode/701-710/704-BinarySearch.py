class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # binary search with two pointers
        left, right = 0, len(nums) - 1
        while left <= right:  # interval should not be empty
            # Key: left + right might exceed max int boundry,
            # Minus first can be used for larger numbers, results are the same
            mid = left + (right - left) // 2
            if target < nums[mid]:  # target on the left
                right = mid - 1
            elif target == nums[mid]:
                return mid
            else:  # target on the right
                left = mid + 1
        return -1
