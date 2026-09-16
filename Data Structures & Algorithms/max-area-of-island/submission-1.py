class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islandm = 0
        visited = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(visited)
                if (i, j) not in visited and int(grid[i][j]) != 0:
                    #print(i,j)
                    iss = 0

                    queue = []
                    queue.append([i,j])
                    visit = {}

                    while queue:
                        cur = queue.pop()
                        
                        

                        if int(grid[cur[0]][cur[1]]) == 1 and (cur[0], cur[1]) not in visit:
                            iss += 1
                            if cur[0] - 1 >= 0:
                                queue.append([cur[0]-1,cur[1]])
                            if cur[0] + 1 < len(grid):
                                queue.append([cur[0]+1,cur[1]])
                            if cur[1] - 1 >= 0:
                                queue.append([cur[0],cur[1]-1])
                            if cur[1] + 1 < len(grid[0]):
                                queue.append([cur[0],cur[1]+1])
                        
                        visit[(cur[0], cur[1])] = True
                        visited[(cur[0], cur[1])] = True
                    if iss > islandm:
                        islandm = iss
        return islandm