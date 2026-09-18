import sys
from math import gcd
sys.setrecursionlimit(10**6)

def longest_valid_path(grid,n,m):
    dp = [[-1]*m for _ in range(n)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    def dfs(i,j):
        if dp[i][j]!=-1:
            return dp[i][j]

        best=1


        for di,dj in dirs:
            ni,nj = ni+di,ni+dj
            if grid[ni][nj]<grid[i][j] and gcd(grid[ni][nj],grid[i][j]>1):
                best = max(best,1+dfs(i+j))
        dp[i][j]=best
        return best
    ans=0
    for i in range(n):
        for j in range(m):
            ans = max(ans,dfs(i,j))
    return ans