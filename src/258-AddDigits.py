class Solution:
    """LOOP"""
    def addDigits(self, num: int) -> int:
        # loop
        while num >= 10:
            num = sum(int(n) for n in str(num))
        return num


class Solution2:
    """RECURSION, much faster, using extra space."""
    def addDigits(self, num: int) -> int:
        # recursion termination
        if len(str(num)) < 2:
            return num
        return self.addDigits(sum([int(n) for n in str(num)]))


class Solution3:
    """O(1), no loop, no recursion, only DECIMAL CALCULATION."""
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num:
                total += num % 10
                num //= 10
            num = total
        return num
