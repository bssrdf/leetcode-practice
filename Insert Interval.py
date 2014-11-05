class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        if len(intervals) == 1: return intervals
        res = []; 
        start = intervals[0].start; end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start <= end and intervals[i].start >= start:
                end = max(end, intervals[i].end)
            else:
                res.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end
        res.append(Interval(start, end))
        return res

if __name__ == "__main__":
    class Interval:
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e
    s = Solution()
    res = s.insert([Interval(1,3), Interval(6, 9)], Interval(2,5))
    for i in res:
        print i.start, i.end