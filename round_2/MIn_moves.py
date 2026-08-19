from collections import deque


def min_moves(n, a):
    if n <= 0 or not a:
        return -1

    start = 0
    if a[start] == 0:
        return 0

    visited = [False] * n
    visited[start] = True
    queue = deque([(start, 0)])

    while queue:
        position, moves = queue.popleft()
        step = a[position]

        for next_position in (position + step, position - step):
            if 0 <= next_position < n and not visited[next_position]:
                if a[next_position] == 0:
                    return moves + 1
                visited[next_position] = True
                queue.append((next_position, moves + 1))

    return -1


print(min_moves(5, [3, 4, 2, 1, 0]))
