"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0
        start = []
        intervals.sort(key=lambda i: i.start)
        for interval in intervals:
            start.append(interval.start)
        end = []
        intervals.sort(key=lambda i: i.end)
        for interval in intervals:
            end.append(interval.end)
        i = 0
        j = 0
        while i < len(start):
            s = start[i]
            e = end[j]
            if s < e:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)
        return res
                



            