import sys

# yes = 1, no = 0
input = sys.stdin.readline
n_cur = int(input())
cur_ls = list(map(int, input().split()))
# 121312
# 1 1 : yes
# 1 2 : no -> 새로 생긴 2가 앞의 1과 같지 않아서 no
# 1 3 : yes-> 새로 생긴 1이 *맨앞의 1과 같은데* *2 2가 yes라서* yes
# 1 4 : no -> 새로 생긴 3이 맨앞의 1과 같지 않아서 no
# 1 5 : no -> 새로 생긴 1이 *맨앞의 1과 같은데* *2 4가 no라서* no
# 1 6 : no

dp = [[-1 for _ in range(len(cur_ls) + 1)] for _ in range(len(cur_ls) + 1)]
for y in range(len(cur_ls) + 1):
    for x in range(len(cur_ls) + 1):
        if (x == y) and x != 0:
            dp[y][x] = 1
#    e0 e1  2  3  4  5  6
# s0 -1 -1 -1 -1 -1 -1 -1
# s1 -1  1 -1 -1 -1 -1 -1
#  2 -1 -1  1 -1 -1 -1 -1
#  3 -1 -1 -1  1 -1 -1 -1
#  4 -1 -1 -1 -1  1 -1 -1
#  5 -1 -1 -1 -1 -1  1 -1
#  6 -1 -1 -1 -1 -1 -1  1

for s in range(len(cur_ls) + 1, 0, -1):
    for e in range(s + 1, len(cur_ls) + 1):
        if (s != e) and (s < e):  # s = 1, e = 2 / s=1, e=3
            if cur_ls[e - 1] == cur_ls[s - 1]:  # e-1 = 1, s-1=0 / e-1 = 2, s-1 = 0
                if e - s > 1:  # 검사할만한게 존재하면
                    if dp[s + 1][e - 1] == 1:
                        dp[s][e] = 1
                    else:
                        dp[s][e] = 0
                else:
                    dp[s][e] = 1
            else:
                dp[s][e] = 0
            pass


n_tk = int(input())
for _ in range(n_tk):
    s, e = map(int, input().split())
    print(dp[s][e])
