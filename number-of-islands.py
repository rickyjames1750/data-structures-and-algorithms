class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        def sinkIsland(grid, r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
            else:
                return
            if r + 1 < len(grid):
                sinkIsland(grid, r + 1, c)
            if r - 1 >= 0:
                sinkIsland(grid, r - 1, c)
            if c + 1 < len(grid[0]):
                sinkIsland(grid, r, c - 1)
            if c - 1 >= 0:
                sinkIsland(grid, r, c - 1)
        counter = 0
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        counter += 1
                        sinkIsland(grid, i, j)
        return counter