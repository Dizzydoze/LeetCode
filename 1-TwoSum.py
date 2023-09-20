class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # hash table
        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return idx, dic[target-num]
            dic[num] = idx