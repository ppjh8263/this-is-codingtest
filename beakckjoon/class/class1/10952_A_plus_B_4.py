import sys
input = lambda :sys.stdin.readline().rstrip()

result = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        result.append(a+b)

for r in result:
    print(r)