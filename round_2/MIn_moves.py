from collections import deque


def min_moves(n, a, start):
    if a[start] == 0:
        return 0

    visited = [False] * n
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        pos, moves = queue.popleft()

        for nxt in [pos + a[pos], pos - a[pos]]:
            if 0 <= nxt < n and not visited[nxt]:
                if a[nxt] == 0:
                    return moves + 1
                visited[nxt] = True
                queue.append((nxt, moves + 1))

    return -1

print(min_moves(5, [2, 3, 0, 1, 4], 0))
print(min_moves(5, [3, 1, 0, 2, 4], 4))