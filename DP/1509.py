s = input().strip()
n = len(s)

is_palindrome = [[False] * n for _ in range(n)]

for i in range(n):
    is_palindrome[i][i] = True

for i in range(n - 1):
    if s[i] == s[i + 1]:
        is_palindrome[i][i + 1] = True

for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
            is_palindrome[i][j] = True

dp = [float("inf")] * n

for i in range(n):
    if is_palindrome[0][i]:  # 처음부터 i까지가 팰린드롬이면
        dp[i] = 1
    else:
        for j in range(i):
            if is_palindrome[j + 1][i]:  # j+1부터 i까지가 팰린드롬이면 count+1
                dp[i] = min(dp[i], dp[j] + 1)

print(dp[n - 1])
