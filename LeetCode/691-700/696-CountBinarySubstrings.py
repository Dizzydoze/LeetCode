class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # count same continuous seperately and store
        # number of kinds of substrings depends on shortest sequence
        prev_cnt, cur_cnt = 0, 1    # initial cur_cnt is 1
        res = 0                     # store the valid substring count answer
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_cnt += 1
            else:
                res += min(prev_cnt, cur_cnt)
                prev_cnt = cur_cnt  # store cur_cnt and move on
                cur_cnt = 1        # reset current count for new number
        # there's no more different number to activate the last min count when the loop ends, so we activate the last count once more
        res += min(prev_cnt, cur_cnt)
        return res
