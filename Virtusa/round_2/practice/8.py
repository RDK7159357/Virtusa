from collections import deque

def Min_moves(a,n,start):
    if a[start]==0:
        return 0
    q = deque()
    visited = [False]*n
    q.append((start,0))
    while q:
        pos,moves = q.popleft()

        for nxt in [[pos+a[pos]],[pos-a[pos]]]:
            if 0<=nxt<n and not visited[pos]:
                if a[pos]==0:
                    return moves+1
                visited[nxt]=True
                q.append((nxt,moves+1))
    return -1
