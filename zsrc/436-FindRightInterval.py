class Solution:
    """sorting, binary search"""
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # sorting sort by end time
        n = len(intervals)
        # store original index [start, end, idx]
        for idx, interval in enumerate(intervals):
            interval.append(idx)
        # intervals sort by start
        intervals.sort()
        # answer list
        res = [-1] * n
        for _, end, idx in intervals:
            # use binary search to find intersion index of end, intervals[i][0] < end
            i = bisect_left(intervals, [end])
            # if insert index i == n, out of index, means no starts in intervals are bigger than current end
            if i < n:
                # res[idx] original place current interval is stored
                # intervals[i][2] the original index of the first interval with the bigger end
                res[idx] = intervals[i][2]
        return res
