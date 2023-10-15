class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # cast all int in list to be string
        strs = [str(n) for n in nums]

        # cmp: compare two string combinations
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        # cmp_to_key transform cmp func into a callable func used by sort()
        strs.sort(key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'
