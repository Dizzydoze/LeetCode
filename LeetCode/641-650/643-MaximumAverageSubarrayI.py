class Solution:
    def findMaxAverage(self, nums, k) -> float:
        # two pointers sliding window, width = k
        # remove pre, add new, don't need to sum every time
        s = sum(nums[:k])
        res = s
        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i-k]  # key point
            res = max(res, s)
        return res/k
