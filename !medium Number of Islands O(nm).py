def numIslands(self, grid: List[List[str]]) -> int:
    islands, way = 0, ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
            grid[x][y] = None

            for i, j in way:
                dfs(x + i, y + j)
            

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            islands += grid[x][y] == '1'
            dfs(x, y)
                
    return islands
