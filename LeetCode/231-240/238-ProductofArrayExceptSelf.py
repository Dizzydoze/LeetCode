class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # DP, similar to climbing steps
        # calculate from LEFT and RIGHT separately
        n = len(nums)
        # products [1, 1, 1, 1]
        # nums     [3, 4, 2, 5]
        # LEFT: multiplying FORWARD, each idx is the product of all previous idxs
        # products[i] = product of all the numbers in nums[:i]
        products = [1] * n
        for i in range(1, n):
            products[i] = products[i - 1] * nums[i - 1]
        # RIGHT: multiplying BACKWARD, store the product of all previous idxs in right
        right = nums[-1]
        for i in range(n - 2, -1, -1):
            products[i] = products[i] * right
            # right = product of all the numbers in nums[:i+1]
            right = right * nums[i]
        return products
