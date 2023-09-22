class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # two pointers
        high, low = 0, 0
        res = []
        prev = inf
        while low < len(s):
            if s[low] == c:
                while high <= low:
                    dis = min(abs(high - low), abs(high - prev))
                    res.append(dis)
                    high += 1
                prev = low  # mark as previous char for comparison
            low += 1
        # process the rest of the list
        while high < len(s):
            res.append(abs(high-prev))
            high += 1
        return res
