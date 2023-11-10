class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two pointers
        left, right = 0, 0
        # Increase left if a match found, otherwise keep looking up in right
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1
        # Left reach the end if all chars in substring have been found
        return left == len(s)
