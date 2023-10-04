class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        res = "" + s[:2]
        for i in range(2, len(s)):
            if not s[i] == s[i - 1] == s[i - 2]:
                res += s[i]
        return res


class SolutionFaster:
    """Much faster, counting repetition."""
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        prev, count, res = "", 1, ""
        # count repeated times
        for ch in s:
            if ch == prev:
                count += 1
            else:
                # reset count if differ
                count = 1
            if count < 3:
                res += ch
            # update current char as previous
            prev = ch
        return res
