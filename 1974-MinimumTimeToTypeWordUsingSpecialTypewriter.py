class Solution:
    def minTimeToType(self, word: str) -> int:
        # abs, two parts of a circle.
        count = len(word)  # tpying cost 1 sec each
        cur = "a"
        for ch in word:
            distance = abs(ord(ch) - ord(cur))
            min_dis = min(distance, 26 - distance)  # cur half or other half
            count += min_dis
            cur = ch  # update cur char
        return count
