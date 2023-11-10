class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # similar to merge sorted lists
        res = ""
        l, r, ln, rn = 0, 0, len(word1), len(word2)
        while l < ln and r < rn:
            res += word1[l]
            res += word2[l]
            l += 1
            r += 1
        # rest of l
        while l < ln:
            res += word1[l]
            l += 1
        # rest of r
        while r < rn:
            res += word2[r]
            r += 1
        return res
