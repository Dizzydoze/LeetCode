class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Count with hash map
        dic = dict()
        for n in nums:
            # return once find duplicates
            if n in dic and dic[n] >= 1:
                return True
            # if key not exist, get 0
            dic[n] = dic.get(n, 0) + 1
        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sort
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
