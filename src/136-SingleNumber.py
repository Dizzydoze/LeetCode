class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR calculation, a XOR b, means bit of a - bit of b
        # XOR between same character or number, result will be 0
        # 3 = 0011, 1 = 0001, 3 ^ 1 = 0010 = 2
        # for all the same num in the list the XOR result is 0,
        # sequence doesn't matter, the only one num left is the answer.
        # 1^1^2^2^4 = 0^0^4 = 4
        x = 0
        for num in nums:
            x ^= num
        return x
