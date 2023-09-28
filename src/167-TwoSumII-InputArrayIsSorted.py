class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            # too big, move big num left to become smaller
            if s > target:
                r -= 1
            # too small, move small num right to become bigger
            elif s < target:
                l += 1
            # match found, return +1 index as required
            else:
                return [l + 1, r + 1]
        # loop ends with no match, return empty listt
        return []
