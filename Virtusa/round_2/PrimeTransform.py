from collections import deque


def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, so it's not prime
            
    return True  # No divisors found, it is prime


def prime_transform(n, k):
    s = str(n)
    q = deque([(s, 0)])
    seen = {s: 0}
    best = -1

    while q:
        curr, ops = q.popleft()
        v = int(curr)
        if is_prime(v) and (best == -1 or v < best):
            best = v
        if ops == k: continue
        for i, d in enumerate(curr):
            for nd in (int(d) - 1, int(d) + 1):
                if nd < 0 or nd > 9 or (i == 0 and nd == 0):
                    continue
                nxt = curr[:i] + str(nd) + curr[i + 1:]
                nops = ops + 1
                if nops <= k and (nxt not in seen or nops < seen[nxt]):
                    seen[nxt] = nops
                    q.append((nxt, nops))
    return best


print(prime_transform(231, 2))