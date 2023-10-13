class Solution:
    """sorting + two pointers; 3sum + 1 more loop"""
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = list()
        # fisrt num i
        for i in range(n):
            # skip duplications
            if i > 0 and nums[i] == nums[i - 1]: continue
            # second num k
            for k in range(i + 1, n):
                # skip duplications
                if k > i + 1 and nums[k] == nums[k - 1]: continue
                # two pointers
                l, r = k + 1, n - 1
                while l < r:
                    # move right backward if too big
                    if nums[i] + nums[k] + nums[l] + nums[r] > target:
                        r -= 1
                    # move left forward if too small
                    elif nums[i] + nums[k] + nums[l] + nums[r] < target:
                        l += 1
                    # target found
                    else:
                        res.append([nums[i], nums[k], nums[l], nums[r]])
                        # skip duplication, remember l < r condition
                        while l < r and nums[l + 1] == nums[l]: l += 1
                        while l < r and nums[r - 1] == nums[r]: r -= 1
                        # only move both pointers if target is found
                        l += 1
                        r -= 1
        return res


class Solution2:
    """Hash table count nums,  3 loops, check distinct nums count to avoid duplicates"""
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # hash table + 3 loops; O(n^3)
        n = len(nums)
        # use set to avoid duplicates
        res = set()
        # hash table store num:count
        cnts = dict()
        for num in nums:
            if num in cnts:
                cnts[num] += 1
            else:
                cnts[num] = 1

        # 3 loops, find difference in hash table
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in cnts:
                        # avoid index duplicates, equal is 1, unequal is 0
                        distinct_cnt = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        # there are enough distinct vals
                        if cnts[val] > distinct_cnt:
                            # sort it for set to filter duplicates
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
        # chagne set back into list
        return list(res)




