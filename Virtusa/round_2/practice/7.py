def max_reward(a,n):
    if n==0:return -1
    if n==1: return a[0]

    dp = [0]*(n+3)

    for i in range(n):
        skip = dp[i+2]
        take = a[i]+dp[i+1]

        take_pair=0

        if i>0 and a[i-1]<0:
            take_pair = a[i]+a[i-1]+dp[i]
        dp[i+3] =max(take_pair,take,skip)

    return dp[n+2] 
