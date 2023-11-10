class Solution:
    """hash table"""
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        print(d)
        res = set()
        for num, cnt in d.items():
            if cnt > len(nums) // 3:
                res.add(num)
        return res


class Solution2:
    """using built in collections.Counter"""
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [num for num, cnt in collections.Counter(nums).items() if cnt > len(nums) // 3]
