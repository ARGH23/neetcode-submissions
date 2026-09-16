inf = 2147483647

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = []
        chests = []

        for i in range(len(grid)):
            toa = [False] * len(grid[0])
            visit.append(toa)
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    chests.append([i,j])
        

        nl = chests
        dist = 0

        while nl:
            nnl = []

            for point in nl:
                i = point[0]
                j = point[1]
                if grid[i][j] != -1 and visit[i][j] == False:
                    
                    if i - 1 >= 0:
                        nnl.append([i-1,j])
                    if j - 1 >= 0:
                        nnl.append([i,j-1])
                    if i + 1 < len(grid):
                        nnl.append([i+1, j])
                    if j + 1 < len(grid[0]):
                        nnl.append([i, j+1])
                    if grid[i][j] == inf:
                        grid[i][j] = dist
                    visit[i][j] = True

            dist += 1
            nl = nnl


