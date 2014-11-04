class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0 or len(intervals)==1: return intervals
        intervals.sort(key=lambda x: x.start)
        start = intervals[0].start; end = intervals[0].end
        res = []
        for i in range(1, len(intervals)):
            if intervals[i].start <= end:
                if intervals[i].end > end:
                    end = intervals[i].end
            else:
                new_interval = Interval(start, end)
                res.append(new_interval)
                start = intervals[i].start
                end = intervals[i].end
        res.append(Interval(start, end))
        return res

if __name__ == "__main__":
    class Interval:
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e
    intervals = [Interval(1,4), Interval(0,4)]
    s = Solution()
    result = s.merge(intervals)
    for r in result:
        print r.start, r.end

