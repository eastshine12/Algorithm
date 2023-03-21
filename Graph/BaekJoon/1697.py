import sys

N, K = map(int, sys.stdin.readline().split())
result = 0

while N != K:

    if K/N > 1:
        N *= 2
    elif K > N:
        K -= 1
    else:
        K += 1
    result += 1

print(result)