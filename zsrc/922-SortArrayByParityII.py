class Solution:
    def sortArrayByParityII(self, nums):
        # even, odd index on new res
        res = [0] * len(nums)
        even_idx, odd_idx = 0, 1
        for i in range(len(nums)):
            if nums[i] % 2 == 0:    # even num
                res[even_idx] = nums[i]
                even_idx += 2
            else:  # odd num
                res[odd_idx] = nums[i]
                odd_idx += 2
        return res
