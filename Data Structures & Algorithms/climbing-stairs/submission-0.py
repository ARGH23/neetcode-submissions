class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        


        vals = [0] * n


        vals[-1] = 1
        vals[-2] = 2


        for i in range(-3, -len(vals) - 1, -1):
            vals[i] = vals[i+1] + vals[i+2]
        return vals[0]