class Solution:
    def diStringMatch(self, s):
        # two pointers, lo hi
        lo = 0
        hi = len(s)  # point to last char in res
        res = [0] * (len(s) + 1)  # one more char than string
        for idx, char in enumerate(s):
            if char == "I":
                res[idx] = lo  # always smallest char
                lo += 1
            else:
                res[idx] = hi  # always largest char
                hi -= 1
        res[len(s)] = lo   # last char to add, lo == hi
        return res
