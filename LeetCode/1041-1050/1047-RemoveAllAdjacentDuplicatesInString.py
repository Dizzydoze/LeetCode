class Solution:
    def removeDuplicates(self, s: str) -> str:
        # sliding window
        left = 0
        while left + 1 < len(s):    # left + 1 == window width
            if s[left] == s[left+1]:
                s = s[:left] + s[left+2:]  # slice to remove
                if left > 0:
                    left -= 1  # key point, don't restart from begining, just move 1 step back
            else:
                left += 1   # move until duplicates found
        return s
