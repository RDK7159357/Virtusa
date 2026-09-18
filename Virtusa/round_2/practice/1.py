from itertools import combinations
from math import gcd
def destroy_monsters(a,n):
    arr = a[::-1]
    total_cost=0
    best = float('inf')
    best_pair=None
    cand_idx = list(set([0,size//2,size-1]))
    while len(arr)>0:
        size = len(arr)
        for di,dj in combinations(cand_idx,2):
            g = gcd(arr[di],arr[dj])
            if g<best:
                best = g
                best_pair = (di,dj)
        i,j=best_pair
        total_cost+=best
        for idx in sorted([i,j],reversed=True):
            arr.pop(idx)
    return total_cost