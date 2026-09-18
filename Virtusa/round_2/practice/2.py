import sys

sys.setrecursionlimit(10**6)

def decay_trail(grid,n,m,sx,sy):
    dp = [[-1]*m for _ in range(n)]
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]

    def dfs(i,j):
        if dp[i][j]!=-1:
            return dp[i][j]
        best=1

        for di,dj in dirs:
            ni,nj=ni+di,nj+dj

            if 0<=ni<n and 0<=nj<m:
                if grid[ni][nj]<grid[i][j]:
                    best = max(best,1 + dfs(i,j))
        dp[i][j]=best
        return best
    return dfs(sx,sy)
