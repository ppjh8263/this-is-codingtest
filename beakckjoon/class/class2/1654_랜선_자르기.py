import sys

input = lambda : sys.stdin.readline().rstrip()

K, N = map(int, input().split())

targets = []
for _ in range(K):
    targets.append(int(input()))

max_target = min(targets)
result = 0
for i in range(max_target, 0, -1000):
    tmp_cnt = 0
    for t in targets:
        tmp_cnt += t // i
    if tmp_cnt >= N:
        result = i
        for j in range(i, 1000 + i):
            if tmp_cnt < N:
                result = j
                break   
        break

print(result)