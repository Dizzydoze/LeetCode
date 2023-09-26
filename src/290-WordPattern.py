class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # biobjection, num of patterns == num of words
        words = s.split()
        if len(pattern) != len(words):
            return False
        # hash table
        wordpat = {}  # word: pat
        patword = {}  # pat: word
        # only both ways matches if a perfect match
        for pat, word in zip(pattern, words):
            # if word exists, check if the pattern matches the word
            if word in wordpat.keys() and wordpat[word] != pat:
                return False
            # if pattern exists, check if the word matches the pattern
            if pat in patword.keys() and patword[pat] != word:
                return False
            wordpat[word] = pat
            patword[pat] = word
        return True
