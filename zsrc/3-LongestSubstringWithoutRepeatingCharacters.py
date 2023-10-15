class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # left + 1 to remove, right + 1 to add
        occur = set()
        max_len, right = 0, -1  # start from left side of the string
        for left in range(len(s)):
            if left != 0:   # remove the former ele because repeated
                occur.remove(s[left - 1])
            while right + 1< len(s) and s[right + 1] not in occur:
                # add ele on right + 1 indx into hash set
                occur.add(s[right+1])
                right += 1  # move forward
            max_len = max(max_len, right - left + 1)  # update max len
        return max_len