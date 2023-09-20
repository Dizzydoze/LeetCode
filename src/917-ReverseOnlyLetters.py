class Solution:
    def reverseOnlyLetters(self, s):
        res = [0] * len(s)
        # two pointers
        left, right = 0, len(s) - 1
        while left <= right:
            # directly added if sepecial char
            if not s[left].isalpha():
                res[left] = (s[left])
                left += 1
            elif not s[right].isalpha():
                res[right] = (s[right])
                right -= 1
            # now they are both letter, reverse
            else:
                res[left] = s[right]
                res[right] = s[left]
                left += 1
                right -= 1
        return "".join(res)
