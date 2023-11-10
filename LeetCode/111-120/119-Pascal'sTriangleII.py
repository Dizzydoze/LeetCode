class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # DP, only last row needed, save space to O(1)
        # there are always only 2 elements in res
        res = [[1], [1, 1]]
        for _ in range(2, rowIndex + 1):
            # res[-1] previous row
            # res[-1][j] + res[-1][j-1] sum of each 2 elements in previous row
            # add new row, pop leftmost unnecessary row
            nxt = [1] + [res[-1][j] + res[-1][j-1] for j in range(1, len(res[-1]))] + [1]
            res.append(nxt)
            res.pop(0)
        return res[0] if rowIndex == 0 else res[-1]
