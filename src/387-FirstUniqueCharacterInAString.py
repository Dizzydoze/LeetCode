from math import inf


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # counting with dic
        dic = {}
        min_idx = inf
        res = -1
        for idx, ch in enumerate(s):
            if ch in dic:
                dic[ch][1] += 1
            else:
                dic[ch] = [idx, 1]
        for idx, cnt in dic.values():
            if cnt == 1 and idx < min_idx:
                res = idx
                min_idx = idx
        return res
