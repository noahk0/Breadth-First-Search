def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    way = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(x, y):
        for i, j in way:
            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]) and grid[x][y] + 1 < grid[x + i][y + j]:
                grid[x + i][y + j] = grid[x][y] + 1
                dfs(x + i, y + j)

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not grid[x][y]:
                dfs(x, y)
