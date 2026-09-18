from math import gcd
import sys

sys.setrecursionlimit(10**6)

def longest_valid_path(grid,n,m):
    dp =[[-1]*m for _ in range(n)]

    dirs=[(0,1),(1,0),(0,-1),(-1,0)]

    def dfs(i,j):
        if dp[i][j]!=-1:
            return dp[i][j]
        best=1

        for di,dj in dirs:
            ni,nj = i+di,j+dj

            if 0<=ni<n and 0<=nj<m :
                if grid[ni][nj]<grid[i][j] and gcd(grid[ni][nj],grid[i][j])>1:
                    best = max(best,1+dfs(ni,nj))

        dp[i][j]=best
        return best
    ans=0
    for i in range(n):
        for j in range(m):
            ans=max(ans,dfs(i,j))
    return ans

grid = [[1,2], [5,6],[4,9]]
print(longest_valid_path(grid,3,2))