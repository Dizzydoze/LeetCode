class Solution:
    """sorting"""
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution2:
    """Hash Table + Counting"""
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        # count frequency of char in s
        for c in s:
            d[c] += 1
        # decrease frequency of same char in t
        for c in t:
            d[c] -= 1
        # if there's non-zero frequency, NOT Anagram
        for f in d.values():
            if f != 0:
                return False
        return True
