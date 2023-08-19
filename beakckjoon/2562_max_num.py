import sys
input = sys.stdin.readline
max = -9999
result = -1
for i in range(9):
    n = int(input().rstrip())
    if n > max:
        max = n
        result = i

print(max)
print(result + 1)