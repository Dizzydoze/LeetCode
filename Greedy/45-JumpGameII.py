class Solution:
    """Greedy: jump as far as possible, make sure the next step can reach farthest index"""
    def jump(self, nums: List[int]) -> int:
        # farthest: the farthest index [next step] can reach
        # end: the farthest index [current step] can reach
        steps, farthest, end = 0, 0, 0
        # we are guranteed to reach the end at len(nums) - 2
        for i in range(len(nums) - 1):
            # keep searching for farthest index [next step] can reach
            farthest = max(farthest, i + nums[i])
            # we only jump to the farthest position
            # other time we are just looking for farthest index next step can reach
            if i == end:
                end = farthest
                steps += 1
        return steps
