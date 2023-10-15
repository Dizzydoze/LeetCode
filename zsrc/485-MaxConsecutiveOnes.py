class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:  # reach none 1
                if count > max:
                    max = count  # update max
                count = 0  # reset count no matter what
        # remember to check the last round
        return max if max > count else count
