class Solution:
    def numIdenticalPairs(self, nums) -> int:
        # hashmap stores repeats
        # the i-th repeat num has i-1 combination with previous nums
        repeat = {}
        res = 0
        for num in nums:
            if num not in repeat:
                repeat[num] = 1     # add num to hashmap
            else:
                res += repeat[num]  # good pairs = prev num count
                repeat[num] += 1    # update repeat count
        return res
