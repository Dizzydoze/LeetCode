class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sorted first
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            # impossible for sorted list == 0
            if nums[i] > 0:
                return res
            # skip duplicates, mind index out of range, use minus
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two pointers from each side of the list
            L = i + 1
            R = length - 1
            while L < R:
                # save the matched result
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    # skip duplicates before go in to next loop
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    # move both pointer as there's a match
                    L += 1
                    R -= 1
                # R is too big, move backward
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R -= 1
                # L is too small, move forward
                else:
                    L += 1
        return res
