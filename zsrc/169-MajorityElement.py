from collections import defaultdict


class Solution1:
    # Sort
    def majorityElement(self, nums: list[int]) -> int:
        # sort, majority will definitely at mid-index
        nums.sort()
        return nums[len(nums) // 2]


class Solution2:
    # HashMap
    def majorityElement(self, nums: list[int]) -> int:
        # hashmap count
        length = len(nums)
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1

        mid = length // 2
        for num, count in cnt.items():
            if count > mid:
                return num
        return 0
