class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Counting, HashTable, Sorting
        dic = {}
        curlen = n = len(arr)
        res = 0
        for num in arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        # Sort by value, no need to know the number, just focus on the count
        cnts = sorted([cnt for cnt in dic.values()])[::-1]
        for cnt in cnts:
            curlen -= cnt  # always minus most count first
            res += 1  # size of set + 1
            if curlen <= n // 2:
                return res
