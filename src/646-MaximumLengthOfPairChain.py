from math import inf


class Solution:
    def findLongestChain(self, pairs) -> int:
        chain = 0
        cur = -inf
        for left, right in sorted(pairs, key=lambda pair: pair[1]):
            if cur < left:
                cur = right  # keep changing cur pointer to right element
                chain += 1
        return chain
