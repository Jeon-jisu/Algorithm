import sys, math

input = sys.stdin.readline()
A, B = map(int, input.split())
n = B
isPrime = [False] * (n + 1)
cntPrime = [0] * (n + 1)
isPrime[2] = True
cntPrime[2] = 1
for i in range(3, n + 1):
    isPrime[i] = True
    for e in range(2, int(math.sqrt(i)) + 1):
        if i % e == 0:
            cntPrime[i] = cntPrime[i // e] + 1
            isPrime[i] = False
            break
    if isPrime[i]:
        cntPrime[i] = 1
cnt = 0
for i in range(A, B + 1):
    cnt += isPrime[cntPrime[i]]
print(cnt)
