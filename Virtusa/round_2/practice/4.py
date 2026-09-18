def maxOr(a,n):
    total_or =0
    for x in a:
        total_or|=x

    suffix = [0]*n
    prefix = [0]*n
    prefix[0]=a[0]
    suffix[n-1] = a[n-1]

    for i in range(1,n):
        prefix[i] = prefix[i-1]|a[i]
    for j in range(n-2,-1,-1):
        suffix[j]= suffix[i+1]|a[i]

    max_len=0
    for l in range(n):
        left_or = prefix[l-1] if l>0 else 0
        for r in range(l,n):
            right_or = suffix[i+1] if r<n-1 else 0

            if left_or|right_or ==total_or:
                max_len = max(max_len,r-l+1)
    return max_len