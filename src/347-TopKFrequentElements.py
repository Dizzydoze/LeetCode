class Solution:
    """defaultdict with int"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hash Table
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        ls = sorted([(num, cnt) for (num, cnt) in d.items()], key=lambda x: x[1], reverse=True)
        return [num for num, _ in ls[:k]]


class Solution2:
    """defaultdict with list"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = collections.defaultdict(list)
        for num in nums:
            num_dict[num].append(num)
        # sort all [num list] in [num dic] by length
        val_ls = sorted(num_dict.values(), key=len, reverse=True)
        return [num_ls[0] for num_ls in val_ls][:k]
