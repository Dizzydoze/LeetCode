class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if len(s)< len(p):  # special case
            return res
        s_count, p_count = [0]*26, [0]*26  # two counters
        for i in range(len(p)):  # count letters in p and window s
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        if p_count == s_count:  # match from the start
            res.append(0)

        left, right = 0, len(p)  # two pointers
        # move window forward
        while right < len(s):
            s_count[ord(s[left]) - ord('a')] -=1  # remove left idx letter
            s_count[ord(s[right]) - ord('a')] += 1  # add right idx letter
            if s_count == p_count:  # there's a match
                res.append(left + 1)  # left removed, cur left should be left + 1
            left += 1
            right += 1
        return res
