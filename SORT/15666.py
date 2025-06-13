import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
n, m = map(int, input().split())
ls = list(set(map(int, input().split())))
ls.sort()
ncr = combinations_with_replacement(ls, m)
for i in ncr:
    print(*i, end="\n")

# Take home message
# itertools에서 중복조합활용
# 조합 : combinations
# 순열 : permutation
# 중복순열 : product(iter, repeat=2)
# 중복조합 : combinations_with_replacement
