class SolutionPractice:
    def isPalindrome(self, s: str) -> bool:
        # first loop clean up all non-alpha letters
        clean = list()
        for ch in s.lower():
            if ch.isdigit() or ch.isalpha():
                clean.append(ch)
        # two pointers
        l, r = 0, len(clean) - 1
        while l <= r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        return True


class SolutionOptimized:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for c in s.lower():
            if c.isalnum():
                clean += c
        return True if clean == clean[::-1] else False
