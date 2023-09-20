class Solution:
    def isValid(self, s: str) -> bool:
        # special cases
        if len(s) % 2 != 0:
            return False
        # stack store the left ones
        stack = []
        # use for match check
        dic = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        for item in s:
            if item in dic:  # check stack if there's a match
                if not stack or stack[-1] != dic[item]:  # empty stack or not match
                    return False
                stack.pop()  # remove the match one
            else:
                stack.append(item) # add left ones to stack
        return not stack  # if there's still sth unmatch left in the stack
