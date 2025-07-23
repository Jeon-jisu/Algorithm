n = int(input())
schedule = []
for i in range(n):
    t, p = map(int, input().split())
    schedule.append([t, p])
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    t, p = schedule[i]
    end = i + t
    if end <= n:
        dp[i] = max(dp[end] + p, dp[i + 1])
    else:
        dp[i] = dp[i + 1]
print(dp[0])
