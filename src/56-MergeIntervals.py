class Solution:
    """
    Sort by start
    Storing NON overlapping interval
    Compare top interval in the list
    Update end to further one
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start
        intervals.sort(key=lambda x: x[0])
        # Non overlap interval storage
        res = list()
        for interval in intervals:
            # top interval's end < current start, NO overlap
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # else: interval's end >= current start, overlap
            else:
                # keep change the end time to further one.
                # eg. [1,3] vs. [1,2], should still be 3
                res[-1][1] = max(res[-1][1], interval[1])
        return res
