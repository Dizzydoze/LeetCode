class Solution:
    """
    lost of ways to do it, loop backward, list comprehension, etc.
    """
    def lengthOfLastWord(self, s: str) -> int:
        res, last = 0, False
        # loop from the back
        for i in range(len(s) - 1, -1, -1):
            # s[i] first letter of last word
            if s[i] != " ":
                last = True
                while i >= 0 and s[i] != " ":
                    res += 1
                    i -= 1
            if last:
                return res
