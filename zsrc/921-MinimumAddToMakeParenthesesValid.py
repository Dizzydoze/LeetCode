class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack
        stack = []
        moves = 0
        for p in s:
            if p == "(":
                stack.append(p)
            # there is ( in stack to match
            elif p == ")" and stack:
                stack.pop()
            # nothing in stack to match
            elif p == ")" and not stack:
                moves += 1
        # rest of the p in stack
        for left in stack:
            moves += 1
        return moves

