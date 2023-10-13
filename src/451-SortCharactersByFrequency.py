class Solution:
    """built-in collections.Counter"""
    def frequencySort(self, s: str) -> str:
        d = collections.Counter(s).items()
        sl = sorted([item for item in d], key=lambda x: x[1], reverse=True)
        res = ""
        for c, cnt in sl:
            res += c * cnt
        return res
