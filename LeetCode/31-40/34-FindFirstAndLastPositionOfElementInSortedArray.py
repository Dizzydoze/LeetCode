class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def search(target_num):
            # two pointers
            low, high = 0, len(nums)
            # quit condition low == high, out of boundary
            while low < high:
                mid = (low + high) // 2
                # target on the right side
                if nums[mid] < target_num:
                    low = mid + 1
                # target on the mid or on the left side
                else:
                    high = mid
            # low pointing at the first matched target
            return low

        low = search(target)
        # key point, use target + 1 will find the last occurence
        high = search(target + 1) - 1

        # if lo == hi: there is 1 target
        # if lo < hi: there are multiple targets
        # if lo > hi: there are no targets
        if low <= high:
            return [low, high]
        return [-1, -1]
