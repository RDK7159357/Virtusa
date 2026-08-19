import sys

sys.setrecursionlimit(100000)


def max_decay_trail(grid, n, m, sx, sy):
    dp = [[-1] * m for _ in range(n)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(i, j):
        if dp[i][j] != -1:
            return dp[i][j]

        best = 1

        for di, dj in dirs:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < m:
                if grid[ni][nj] < grid[i][j]:
                    best = max(best, 1 + dfs(ni, nj))

        dp[i][j] = best
        return best

    return dfs(sx, sy)


grid = [[9, 6, 3], [8, 5, 2], [7, 4, 1]]
print(max_decay_trail(grid, 3, 3, 0, 0))