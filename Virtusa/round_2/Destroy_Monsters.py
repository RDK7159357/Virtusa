from itertools import combinations
from math import gcd
def destroy_monsters(n,a):
    arr = a[::-1]
    total_cost = 0
    while(len(arr)>0):
        size=len(arr)
        cand_idx = list(set([0,size//2,size-1]))
        best_gcd = float('inf')

        best_pair=None

        for i,j in combinations(cand_idx,2):
            g = gcd(arr[i],arr[j])
            if g<best_gcd:
                best_gcd = g
                best_pair=(i,j)

        total_cost +=best_gcd
        i,j=best_pair

        for idx in sorted([i,j],reverse=True):
            arr.pop(idx) 
    return total_cost
print(destroy_monsters(5,[2,3,4,5,6]))