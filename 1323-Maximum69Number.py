class Solution:
    def maximum69Number (self, num: int) -> int:
        # change the leftmost 6 to 9
        s = str(num)
        for i in range(len(s)):
            if s[i] == "6":
                return int(s[:i] + "9" + s[i+1:])
        # there's no 6 in whole num
        return num
