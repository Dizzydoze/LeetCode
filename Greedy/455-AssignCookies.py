class Solution:
    def findContentChildren(self, g, s):
        # special case, no cookies
        if len(s) == 0:
            return 0
        # sort first
        g.sort()
        s.sort()
        # two pointers
        chi, coo = len(g) - 1, len(s) - 1
        count = 0
        while chi >= 0 and coo >= 0:
            if s[coo] >= g[chi]:  # satisfied
                count += 1
                coo -= 1  # eaten cookie
                chi -= 1  # satisfied child
            else:
                chi -= 1  # child can never be satisfied
        return count
