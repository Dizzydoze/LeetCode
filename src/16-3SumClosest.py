class Solution:
    """sorting + two pointers"""
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                # too small, move left forward
                if sum3 < target:
                    l += 1
                # too big, move right backward
                else:
                    r -= 1
                # current diff is smaller than previous diff, update new sum3
                if abs(sum3 - target) < abs(closest - target):
                    closest = sum3
        return closest
