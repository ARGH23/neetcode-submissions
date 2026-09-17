class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            grid.append(row)
        
        grid[m-1][n-1] = 1

        #grid[i][j] = grid[i+1][j] + grid[i][j+1]


        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                total = grid[i][j]
                if i+1 < m:
                    total += grid[i+1][j]
                if j+1 < n:
                    total += grid[i][j+1]
                grid[i][j] = total
        
        return grid[0][0]