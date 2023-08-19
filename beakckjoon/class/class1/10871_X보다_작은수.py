import sys
input = lambda : sys.stdin.readline().rstrip()

N, X = map(int, input().split())
result = []
numbers = map(int, input().split())
for n in numbers:
    if n < X:
        result.append(n)

print(' '.join(map(str, result)))