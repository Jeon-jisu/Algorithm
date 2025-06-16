import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
d = int(input())
line = [[] for _ in range(d + 1)]
visited = [-1] * (d + 1)
for idx in range(d):
    k = list(map(int, input().split()))
    for i in range(1, (len(k) - 2), 2):
        line[k[0]].append([k[i], k[i + 1]])


def dfs(start, distance):
    for next, n_dist in line[start]:
        if visited[next] == -1:
            visited[next] = n_dist + distance
            dfs(next, distance + n_dist)


visited[1] = 0
dfs(1, 0)
r_point = visited.index(max(visited))
# print("visited", visited)
visited = [-1] * (d + 1)
visited[r_point] = 0
dfs(r_point, 0)
# print("newvisitied", visited)
print(max(visited))
