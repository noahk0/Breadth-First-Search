def solve(self, board: List[List[str]]) -> None:
    way = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(i, j):
        if board[i][j] == 'O':
            board[i][j] = None

            for x, y in way:
                if 0 <= i + x < len(board) and 0 <= j + y < len(board[0]):
                    dfs(i + x, j + y)

    for i in range(len(board)):
        dfs(i, 0)
        dfs(i, len(board[0]) - 1)

    for i in range(1, len(board[0]) - 1):
        dfs(0, i)
        dfs(len(board) - 1, i)

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = 'X' if board[i][j] else 'O'
