class Solution:
    def distributeCandies(self, candyType) -> int:
        # Count the different types
        unique = set(candyType)   # we can also loop and call set.add()
        uni_count = len(unique)
        eatable = len(candyType)  # 2
        print(uni_count, eatable)
        return eatable if eatable <= uni_count else uni_count

