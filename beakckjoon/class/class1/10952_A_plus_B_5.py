import sys
input = lambda :sys.stdin.readline().rstrip()

result = []
while True:
    try:
        a, b = map(int, input().split())
        result.append(a+b)
    except:
        break
    #     break
    # else:
    #     result.append(a+b)

for r in result:
    print(r)