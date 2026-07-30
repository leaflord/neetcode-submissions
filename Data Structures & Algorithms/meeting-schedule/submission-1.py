class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        return canAttendMeetings(intervals)

def canAttendMeetings(intervals: List[Interval]) -> bool:
    if not intervals:
        return True
    intervals = sorted(intervals, key=lambda t: t.start)
    last = intervals[0]
    for curr in intervals[1:]:
        if last.end > curr.start:
            return False
        last = curr
    return True
