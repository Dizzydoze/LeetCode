class Solution:
    """
    Dynamic Programming
    dp[i][j] = dp[i+1][j+1] + 1
    """
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        res = 0
        # dp list for stroing all previous results
        # we should add one more space for the biggest index to avoid range error
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        # reversely traverse both array
        for i in range(len1 - 1, -1, -1):  # list
            for j in range(len2 - 1, -1, -1):  # nested list
                # the previous index for both array should be i+1 and j+1
                # if num at previous indexes i+1 and j+1 are the same
                # current index i and j should add 1 based on the previous result
                dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                # update current longest same sequence
                res = max(res, dp[i][j])
        return res
