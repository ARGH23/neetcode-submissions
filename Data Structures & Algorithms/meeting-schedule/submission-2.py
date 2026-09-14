"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        intervals = sorted(intervals, key=lambda item: item.start)

        latests = intervals[0].start
        latestf = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < latestf:
                return False
            latests = intervals[i].start
            latestf = intervals[i].end

        
        return True