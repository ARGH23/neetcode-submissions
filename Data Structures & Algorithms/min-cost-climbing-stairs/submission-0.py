class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        vals = [0] * (len(cost) + 1)
        vals[-2] = cost[-1]
        vals[-3] = cost[-2]

        for i in range(-4, -(len(cost) + 2), -1):
            vals[i] = cost[i+1] + min(vals[i+1], vals[i+2])
        
        return min(vals[0], vals[1])