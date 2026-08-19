def decay(grid,m,n):
    dp = [[-1]*m for _ in range(n)]

    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    def dfs(i,j):
        if dp[i][j]!=-1:
            return dp[i][j]

        best=1

        for di,dj in dirs:
            ni,nj = i+di,j+dj

            if 0<=ni<n and 0<=nj<m:
                if grid[ni][nj]<grid[i][j]:
                    best = max(best,1+dfs(ni,nj))

        dp[i][j]=best
        return best
    ans =0
    for i in range(n):
        for j in range(m):
            ans = max(ans,dfs(i,j))
    return ans

print(decay([[1,2], [5,6],[4,9]],3,2))