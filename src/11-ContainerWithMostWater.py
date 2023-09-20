class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Area = (right - left) * min(height[left], height[right])
        max_area = 0
        # Two pointers
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            # Always move the short one, possible to be higher
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
