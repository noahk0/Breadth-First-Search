def orangesRotting(self, grid: List[List[int]]) -> int:
    time, fresh, rot, way = 0, 0, deque(), ((0, 1), (0, -1), (1, 0), (-1, 0))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rot.append((i, j))

            fresh += grid[i][j] == 1

    while rot and fresh:
        for _ in range(len(rot)):
            i, j = rot.popleft()

            for x, y in way:
                if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] == 1:
                    grid[i + x][j + y] = 2
                    rot.append((i + x, j + y))

        time += 1
        fresh -= len(rot)

    return - 1 if fresh else time
