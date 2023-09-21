class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = [0] * 26  # store the ch and its index
        for idx, ch in enumerate(s):
            chars[ord(ch) - ord('a')] = idx  # idx in chars and idx in s
        partition = list()

        # move pointer to current characters last idx, which is the biggest one.
        start = end = 0  # two pointers
        for idx, ch in enumerate(s):
            end = max(end, chars[ord(ch) - ord('a')])
            if end == idx:
                partition.append(end - start + 1)  # size = right - left + 1
                start = end + 1  # start new partition at end + 1
        return partition
