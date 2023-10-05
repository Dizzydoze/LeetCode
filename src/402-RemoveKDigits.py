class Solution:
    """Monotonic Stack"""
    def removeKdigits(self, num: str, k: int) -> str:
        # Monotonic Stack, descending nums
        stack = list()
        for n in num:
            # while stack, there's prev num to compare
            # if k, there's chance to dump num
            # if n < stack[-1], smaller num found, dump the bigger on in the stack
            while stack and k and n < stack[-1]:
                stack.pop()
                k -= 1
            # prevent leading 0 being added into stack
            if stack or n != '0':
                stack.append(n)
        # if k > 0, just dump the last k nums
        if k:
            stack = stack[0: -k]
        return ''.join(stack) or '0'
