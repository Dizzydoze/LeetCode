class Solution:
    """bit manipulation"""
    def findTheDifference(self, s: str, t: str) -> str:
        snum, tnum = 0, 0
        for c in s:
            snum += ord(c)
        for c in t:
            tnum += ord(c)
        return chr(tnum - snum)


class Solution2:
    """sorting"""
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted([c for c in s])
        t = sorted([c for c in t])
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        # or the last char is different
        return t[-1]
