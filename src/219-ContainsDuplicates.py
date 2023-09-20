class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # sliding window width = k + 1
        dup = set()  # hash set for duplication check
        for i in range(len(nums)):
            if i > k:  # i - left > k
                dup.remove(nums[i - k - 1])  # remove the left num
            if nums[i] in dup:  # if the new num in current window set
                return True  # there's a duplication
            dup.add(nums[i])  # else we add the num in to hash set
        return False
