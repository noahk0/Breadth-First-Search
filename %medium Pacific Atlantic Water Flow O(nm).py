def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    pacific, atlantic, way = set(), set(), ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(sea, x, y):
        if (x, y) not in sea:
            sea.add((x, y))

            for i, j in way:
                if 0 <= x + i < len(heights) and 0 <= y + j < len(heights[0]) and heights[x][y] <= heights[x + i][y + j]:
                    dfs(sea, x + i, y + j)

    for x in range(len(heights)):
        dfs(pacific, x, 0)
        dfs(atlantic, x, len(heights[0]) - 1)

    for y in range(len(heights[0])):
        dfs(pacific, 0, y)
        dfs(atlantic, len(heights) - 1, y)

    return pacific & atlantic
