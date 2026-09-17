class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        grid = []
        n = len(s)

        for i in range(n):
            ta = []

            for j in range(n):
                ta.append(0)
            grid.append(ta)
        

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or grid[i+1][j-1] == 1):
                    grid[i][j] = 1
                    total += 1

        return total 