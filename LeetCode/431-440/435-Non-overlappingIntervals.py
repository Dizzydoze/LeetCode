class Solution:
    """sorting"""
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        # sorted by end time
        for s, e in sorted(intervals, key=lambda x: x[1]):
            # if current start >= previous end, no overlap, update new end to cur end
            if s >= end:
                end = e
            # current start < previous end, overlap, count + 1
            else:
                cnt += 1
        # there are cnt interval we need to deal with
        return cnt
