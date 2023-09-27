class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # brute force
        lenn = len(needle)
        lenh = len(haystack)
        # no need to traverse the last word
        for i in range(lenh - lenn + 1):
            # slice
            if haystack[i: i + lenn] == needle:
                return i
        return -1
