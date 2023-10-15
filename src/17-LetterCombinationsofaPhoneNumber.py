class Solution:
    """Backtracking"""
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(digits, index, combination):
            # recursion termination condition
            # it might be an empty digit
            if not digits:
                return ""
            # the length of combination is the length of digits
            if len(combination) == len(digits):
                # add s to the result
                res.append(combination)
                return
            # get current digit
            digit = digits[index]
            # get related letters
            letters = lettersmap[digit]
            # traverse current letters to find combination
            for i in range(len(letters)):
                # add letters[i] to current combination
                # go down to look for digits[index+1] to get the next letter
                backtrack(digits, index + 1, combination + letters[i])

        # hash table stores {num: letters}
        lettersmap = {
            "": "",
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        # combination stores current combination result
        combination = ''
        res = list()
        # digit[0]: start from index 0 which is the first digit
        # the combination is empty at the beginning
        backtrack(digits, 0, combination)
        return res
