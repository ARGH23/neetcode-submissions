class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        first = -1
        last = -1
        maxi = 0


        for i in prices:
            if first == -1:
                first = i
            elif i < first:
                if last == -1:
                    first = i
                else:
                    maxi = max(last - first, maxi)
                    first = i
                    last = -1
            elif i > last:
                last = i
        
        if last != -1:
            maxi = max(last-first, maxi)

        return maxi