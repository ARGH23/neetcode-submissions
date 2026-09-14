class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        ans = []

        before = True
        niadded = False
        for i in intervals:
            if i[1] < newInterval[0] and before:
                ans.append(i)
            
            elif i[1] >= newInterval[0] and i[0] <= newInterval[1] and before:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
                ans.append(newInterval)
                before = False
                niadded = True
            
            elif before:
                ans.append(newInterval)
                ans.append(i)
                before = False
                niadded = True
            

            else:
                if i[0] <= ans[-1][1]:
                    ans[-1][0] = min(ans[-1][0], i[0])
                    ans[-1][1] = max(ans[-1][1], i[1])
                
                else:
                    ans.append(i)
        
        if not niadded:
            ans.append(newInterval)

        return ans

