from collections import deque


def maze(n):
    q = deque()
    for i in range(1, n + 1):
        q.append(i)
    seconds = 0
    while q:
        seconds += 1
        # first person enters
        first = q.popleft()
        if first == n:
            return seconds
        # third person enters
        if len(q) >= 2:
            second = q.popleft()
            third = q.popleft()
            if third == n:
                return seconds
            q.appendleft(second)


# Driver Code / Execution:
n = int(input())
print(maze(n))