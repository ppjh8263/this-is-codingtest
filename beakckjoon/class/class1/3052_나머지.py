import sys

input = sys.stdin.readline
result = set()
N = 10
target = 42
for _ in range(N):
    result.add(int(input().rstrip()) % target)

print(len(list(result)))