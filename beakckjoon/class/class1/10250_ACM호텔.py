import sys

input = sys.stdin.readline
T = int(input().rstrip())
inputs = []
for _ in range(T):
    inputs.append(map(int, input().split()))
for h, w, n in inputs:
    stair = n % h
    if stair == 0:
        stair = h
    num = n // h 
    if num == 
    print(f"{()}{str(n // h  + 1).zfill(2)}")

1010