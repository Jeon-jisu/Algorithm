import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
mapp = []
for _ in range(n):
    mapp.append(list(map(int, input().rstrip())))


def bfs():
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        cur = q.popleft()
        cur_x = cur[0]
        cur_y = cur[1]
        for i in range(4):
            next_x = cur[0] + dx[i]
            next_y = cur[1] + dy[i]
            if (
                (0 <= next_x < m)
                and (0 <= next_y < n)
                and (visited[next_y][next_x] == -1)
                and (mapp[next_y][next_x] == 1)
            ):
                if (next_x == m - 1) and (next_y == n - 1):
                    visited[next_y][next_x] = visited[cur_y][cur_x] + 1
                    print(visited[next_y][next_x])
                    return
                else:
                    visited[next_y][next_x] = visited[cur_y][cur_x] + 1
                    q.append([next_x, next_y])


bfs()
