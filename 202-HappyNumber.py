class Solution:
    def isHappy(self, n: int) -> bool:
        count = n
        prev = set()  # store previous square results
        while count != 1:  # keep updating count until it reaches 1 or reappears
            count = sum([int(num)**2 for num in str(count)])
            if count not in prev:
                prev.add(count)
            else:  # it's a loop
                return False
        return True
