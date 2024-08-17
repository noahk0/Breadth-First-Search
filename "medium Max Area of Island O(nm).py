def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    large = 0
        
    def dfs(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:
            grid[x][y] = 0
            return dfs(x, y + 1) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x - 1, y) + 1

        return 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            large = max(large, dfs(x, y))

    return large
