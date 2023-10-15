class Solution:
    """Much less space usage, slower"""
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(2, len(arr)):
            if arr[i] % 2 != 0 and arr[i - 1] % 2 != 0 and arr[i - 2] % 2 != 0:
                return True
        return False


class Solution2:
    """Much Faster, using extra space"""
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return "111" in "".join([str(n%2) for n in arr])