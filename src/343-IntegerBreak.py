class Solution:

    def integerBreak(self, n: int) -> int:
        # DP, bottom-top, n = 4 is good for drafting the solution
        # memo[i] stores max splited product of number i, each slot is max product
        memo = [-1] * (n + 1)
        # 1 can't be split anymore
        memo[1] = 1
        # split starts from 2 to n
        for i in range(2, n + 1):
            # each num i can be splited into j, i - j, until i - 1
            for j in range(1, i):
                # j * (i-j) split into 2 parts and stop
                # KEYPOINT: memo[i-j] stores number "i-j" max product
                # j <= i - 1, then i - j >= 1, always start from idx 1
                # j * memo[i-j] split into 2 parts and keep spliting
                # each i's product with j=1, j=2,...j=i-1, keep comparing to find max
                memo[i] = max(memo[i], j*(i-j), j*memo[i-j])
        return memo[n]
