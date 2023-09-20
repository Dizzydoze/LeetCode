class Solution:
    def compress(self, chars):
        # two pointers
        count = 1
        length = len(chars)
        write = 0
        # i for reading, j for writing
        for read in range(length):
            # read pointer reach the end of list(all the same char)
            # or find differ char
            if read == length - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                # adding count number to the list
                if count > 1:
                    for num in str(count):
                        chars[write] = num
                        write += 1
                # reset count for new char
                count = 1
            else:
                # same char
                count += 1
        return write
