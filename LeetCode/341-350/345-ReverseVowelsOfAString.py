class Solution:
    def reverseVowels(self, s: str) -> str:
        # two pointers
        vowels = ["a", "A", "e", "E", "i", "I","o", "O", "u", "U"]
        sl = [c for c in s]
        left, right = 0, len(s) - 1
        while left < right:
            # move until vowels found
            if sl[left] not in vowels:
                left += 1
                continue
            if sl[right] not in vowels:
                right -= 1
                continue
            # switch and move both pointers
            sl[left], sl[right] = sl[right], sl[left]
            left += 1
            right -= 1
        return "".join(sl)
