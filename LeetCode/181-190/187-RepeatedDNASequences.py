class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # sliding window and hash table
        L = 10
        res = list()
        cnt = defaultdict(int)
        # start at 9, 9-10+1 = 0, 9+1 = 10, 0 to 9
        for i in range(L-1, len(s)):
            curr = s[i - L + 1: i + 1]
            cnt[curr] += 1
            if cnt[curr] == 2:
                res.append(curr)
        return res
