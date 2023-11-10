class Solution:
    """DP + bit manipulation
    >> x bit shift x steps to right
    odd  5 >> 1  0101 --> 010  (5 & 1) --> 0101 --> 1
         XOR calculation                   0001
    even 4 >> 1  0100 --> 010  (4 & 1) --> 0100 --> 0
         XOR calculation                   0001
    for odd num:  i >> 1 = i//2
    for even num: i >> 1 = i/2
    1 = 0 + 1
    2 = 1 + 0     even same amount of 1 as i/2
    3 = 1 + 1     odd  same amount of 1 as i/2 + 1
    4 = 2 + 0     even same amount of 1 as i/2
    5 = 2 + 1     odd  same amount of 1 as i/2 + 1
    """
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        # from 1 to n
        for i in range(1, n + 1):

            res[i] = res[i >> 1] + (i & 1)
        return res


class Solution2:
    """binary bin()"""
    def countBits(self, n: int) -> List[int]:
        return [collections.Counter(bin(i)[2:])['1'] for i in range(n + 1)]
