import sys

input = sys.stdin.readline
k = input().split()
n, m = int(k[0]), int(k[1])
st_l = {}
for _ in range(n):
    t = input().split()
    st_l[t[0]] = t[1]
for _ in range(m):
    key = input().strip()
    print(st_l[str(key)])

# Take home message
# strip으로 양옆 공백 제거
