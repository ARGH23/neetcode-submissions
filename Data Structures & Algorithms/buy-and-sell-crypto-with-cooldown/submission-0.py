class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #maxProfit[i,j] i = current day, j = purchase day, -1 if none
        #either we can sell and then profit is diff + maxprofit[i+2, -1] or we can hold[i+1, j]
        #if buying can either pass maxProfit[i+1, -1] or buy maxprofit[i+1, i]
        #base case is maxprofit[any, last day] = diff
        # maxprofit[any, -1] = 0


        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)
        print(dp)
        return dp[0][1]
        