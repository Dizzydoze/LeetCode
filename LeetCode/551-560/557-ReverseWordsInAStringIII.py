class Solution1:
    # Slice
    def reverseWords(self, s: str) -> str:
        # slice, no extra space
        return " ".join(word[::-1] for word in s.split(" "))


class Solution2:
    def reverseWords(self, s: str) -> str:
        # split, two pointers, extra space
        res = []
        for w in s.split(" "):
            l, r = 0, len(w) - 1
            sl = [ch for ch in w]  # string can't reassign
            while l < r:
                sl[l], sl[r] = sl[r], sl[l]  # switch place
                l += 1
                r -= 1
            res.append("".join(sl))
        return " ".join(res)