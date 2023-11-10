class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # DP, total numRows elements
        res = [[1], [1, 1]] + [-1] * (numRows - 2)
        for i in range(2, numRows):
            # res[i - 1] previous row
            # res[i-1][j] + res[i-1][j-1] each sum of 2 elements in previous row
            new_cont = [res[i-1][j] + res[i-1][j-1] for j in range(1, len(res[i - 1]))]
            res[i] = [1] + new_cont + [1]
        return res[:numRows]
