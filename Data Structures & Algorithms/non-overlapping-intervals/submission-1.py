class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda item:item[0])
        
        count = 0
        prev = float('-inf')

        for start, end in intervals:
            if start >= prev:
                prev = end
            else:
                prev = min(prev, end)
                count += 1
        
        return count

