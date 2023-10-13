class Solution:
    """bit manipulation"""
    def findTheDifference(self, s: str, t: str) -> str:
        snum, tnum = 0, 0
        for c in s:
            snum += ord(c)
        for c in t:
            tnum += ord(c)
        return chr(tnum - snum)
