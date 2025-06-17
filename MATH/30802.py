import sys

input = sys.stdin.readline
n = int(input())
t_list = list(map(int, input().split()))
t, p = map(int, input().split())
t_cnt = 0
for t_each in t_list:
    t_cnt += (t_each) // t
    if (t_each) % t != 0:
        t_cnt += 1
p_cnt = n // p
p_each = n % p
print(t_cnt)
print(p_cnt, p_each)
