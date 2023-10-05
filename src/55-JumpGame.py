class MySolution:
    """Same logic, traverse reversely"""
    def canJump(self, nums: List[int]) -> bool:
        # traverse reversely
        target = len(nums) - 1
        cur = target - 1
        while target >= 1:
            # can't reach target from cur, keep looking backward
            while nums[cur] < target - cur and cur >= 0:
                cur -= 1
            # all spots before target can't reach target with one jump
            if cur < 0:
                return False
            # update target to cur and see if we can reach it again
            i = cur
            cur = i - 1
        return True


class Solution:
    """Same logic, traverse reversely"""
    def canJump(self, nums: List[int]) -> bool:
        # traverse reversely
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # i: current idx; nums[i]: longest jump;
            # update target to current idx to see if we can reach it again
            if i + nums[i] >= target:
                target = i
        # the target will be updated to 0 if we can reach it from the start
        return target == 0