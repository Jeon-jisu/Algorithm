import sys, math

input = sys.stdin.readline
x, y = map(int, input().split())
original = (y * 100) // x
ans = x
if original >= 99:
    print("-1")
else:
    l, r = 1, x
    while l <= r:
        mid = (l + r) // 2
        new = (y + mid) * 100 // (x + mid)
        if new > original:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
