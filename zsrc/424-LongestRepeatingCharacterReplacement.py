class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num_count = [0] * 26  # count occurrence of 26 letters
        left, right = 0, 0  # two pointers
        maxn = 0  # within current window, letter at right idx shows up count

        while right < len(s):
            # count of right idx num + 1
            num_count[ord(s[right]) - ord("A")] += 1
            # update the count of repeating letter everytime we update count
            maxn = max(maxn, num_count[ord(s[right]) - ord("A")])
            # total num in window - length of repeating num > k, no more replace
            if right - left + 1 - maxn > k:
                # remove the left index num from count
                num_count[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        return right - left  # the size of window
