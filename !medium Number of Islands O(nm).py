def numIslands(self, grid: List[List[str]]) -> int:
    islands, way = 0, ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(x, y):
        grid[x][y] = None

        for i, j in way:
            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]) and grid[x + i][y + j] == '1':
                dfs(x + i, y + j)
            

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '1':
                dfs(x, y)
                islands += 1
                
    return islands
