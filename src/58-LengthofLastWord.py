class Solution:
    """
    lost of ways to do it, two pointers, list comprehension, etc.
    """
    def lengthOfLastWord(self, s: str) -> int:
        # two pointers up and down
        u = d = len(s) - 1
        while True:
            # last word found as reaching non-empty spot
            if s[d] != " ":
                # u start to measure length
                u = d
                while u >= 0:
                    if s[u] != " ":
                        u -= 1
                    # last word ends as we reach empty again
                    else:
                        return d - u
                # u < 0, there's only one word in the list
                return d - u
            # moving d backward to find the last word
            else:
                d -= 1
