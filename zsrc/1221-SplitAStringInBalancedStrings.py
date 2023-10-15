class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # cut as long as we can cut
        r, l, res = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "R":
                r += 1
            else:
                l += 1
            if r == l:  # check every loop
                res += 1
        return res
