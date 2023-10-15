class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = 200
        shortest_word = min(strs, key=len)
        for word in strs:
            idx = 0
            for i in range(len(shortest_word)):
                if word[i] != shortest_word[i]:
                    break
                idx += 1
            # update shortest prefix
            prefix = min(prefix, idx)
        return shortest_word[:prefix]
