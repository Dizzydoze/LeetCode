class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # sliding window
        cnt = 0
        min_cnt = 100
        for idx, ch in enumerate(blocks):
            if ch == "W":
                cnt += 1
            # every time move out of window
            # check element just out of the left side of window is W or NOT
            if idx >= k and blocks[idx - k] == "W":
                cnt -= 1  # idx-k not in the window anymore
            if idx >= k - 1:  # first time reach width k, start to count
                min_cnt = min(cnt, min_cnt)
        return min_cnt
