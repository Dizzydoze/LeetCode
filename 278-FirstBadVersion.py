# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Binary Search with Two Pointers
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):  # answer in [left, mid]
                right = mid
            else:  # answer in [mid+1, right]
                left = mid + 1
        # left == right is the answer
        return left
