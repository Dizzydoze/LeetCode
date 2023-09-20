class Solution:
    def splitNum(self, num: int) -> int:
        # greedy, sort first
        nums = sorted([n for n in str(num)])
        left, right = "", ""
        for i in range(len(nums)):
            if i % 2 == 0:
                left += nums[i]
            else:
                right += nums[i]
        return int(left) + int(right)
