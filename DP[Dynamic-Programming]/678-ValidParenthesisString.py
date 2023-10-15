class Solution:
    def checkValidString(self, s: str) -> bool:
        # double stack
        left = list()
        star = list()
        for i in range(len(s)):
            # since * must be on the right of '(', store idx to compare
            if s[i] == '(':
                left.append((i, s[i]))
            elif s[i] == '*':
                star.append((i, s[i]))
            # use '(' first, because * is versatile
            elif s[i] == ')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                # stacks are both empty, no more matches
                else:
                    return False
        # there's sequence among star sign, do not count them
        # handle '(' first, star sign must be on the right side of '(' to match
        while left:
            if star and star[-1][0] > left[-1][0]:
                left.pop()
                star.pop()
            # no more star to match as ')', or star is on the left of a '('
            else:
                return False
        # star can be treated as ""
        return True
