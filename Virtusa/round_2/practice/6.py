def subnum(n,k):
    digits = str(n)
    d = len(digits)
    best = None

    for mask in range(1<<d):

        sub=""
        for i in range(d):
            if mask & i<<d:
                sub +=digits[i]
        if not sub: continue
        if sub[0]=='0': continue
        num = int(sub)
        if num>k:
            if best is None or num<best:
                best = num
    return best if best is not None else -1