import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    f, s, g, u, d = map(int, input().split())
    if s == g:
        print(0)
        return
    q = deque([s])
    visited = [-1] * (f + 1)
    visited[s] = 0
    while q:
        cur = q.popleft()
        if u > 0:
            n_f = cur + u
            if n_f <= f and visited[n_f] == -1:
                visited[n_f] = visited[cur] + 1
                if n_f == g:
                    print(visited[n_f])
                    return
                q.append(n_f)
        if d > 0:
            n_f = cur - d
            if n_f >= 1 and visited[n_f] == -1:
                visited[n_f] = visited[cur] + 1
                if n_f == g:
                    print(visited[n_f])
                    return
                q.append(n_f)
    print("use the stairs")


bfs()
