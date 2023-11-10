class Solution:
    def decodeString(self, s: str) -> str:
        # stack
        stack = list()
        for i in range(len(s)):
            # adding all elements into stack until we meet ']'
            if s[i] != ']':
                stack.append(s[i])
            # start to pop, check the top
            else:
                cur_s = ""
                while stack[-1] != '[':
                    cur_s = stack.pop() + cur_s
                # pop the '[' out
                stack.pop()
                # current counts of copies
                cnt = ""
                # loop until it's not int
                while stack and stack[-1].isdigit():
                    cnt = stack.pop() + cnt
                cur_copies = int(cnt) * cur_s
                # KEYPOINT: add the decode string back into stack
                stack.append(cur_copies)
        return "".join([c for c in stack])
