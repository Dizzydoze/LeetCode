class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window
        # first 3 letters
        cnt = 0
        for i in range(k):
            if s[i] in "aeiou":
                cnt += 1
        max_cnt = cnt
        # rest of letters
        for i in range(k, len(s)):
            if s[i] in "aeiou":
                cnt += 1
            if s[i - k] in "aeiou":
                cnt -= 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt
