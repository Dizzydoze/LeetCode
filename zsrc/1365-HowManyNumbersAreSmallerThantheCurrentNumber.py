class Solution1:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Brute Force
        n = len(nums)
        res = list()
        for i in range(n):
            cnt = 0
            # start from the same idx, fine with condition
            for j in range(n):
                if nums[i] > nums[j]:
                   cnt += 1
            res.append(cnt)
        return res


class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sort and HashTable
        # Index of current num is exactly the Count of smaller nums
        s_nums = sorted(nums)
        dic = dict()
        for i in range(len(s_nums)):
            if s_nums[i] not in dic:    # be careful, same num should have same count
                dic[s_nums[i]] = i
        return [dic[nums[i]] for i in range(len(nums))]
