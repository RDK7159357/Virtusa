def max_reward(a, n):
    n = min(n, len(a))
    if n == 0:
        return 0

    dp = [0] * (n + 3)

    for i in range(n):
        skip = dp[i + 2]
        take = float("-inf")
        take_pair = float("-inf")

        if i == 0 or a[i - 1] >= 0:
            take = a[i] + dp[i + 1]
        elif a[i] >= 0:
            # A negative predecessor must be included and subtracted.
            take_pair = a[i] - a[i - 1] + dp[i + 1]

        dp[i + 3] = max(skip, take, take_pair)

    return dp[n + 2]