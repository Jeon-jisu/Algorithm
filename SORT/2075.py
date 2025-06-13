import heapq
import sys

input = sys.stdin.readline
n = int(input())
max_heap = []
for _ in range(n):
    tmp_l = input().split()
    for k in tmp_l:
        heapq.heappush(max_heap, int(k))
        if len(max_heap) > n:
            heapq.heappop(max_heap)

print(max_heap[0])

# Take home message
# 우선순위 큐, 메모리 초과시 해당 길이를 넘어가면 pop하는 로직
# PriorityQueue는 Thread-safe하다는 점. Lock을 내부적으로 사용해 안정적 heapq는 알고리즘으로 많이 사용
