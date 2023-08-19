import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())

result_dict = {}
for _ in range(N):
    _input = input()
    result_dict[_input] = len(_input)

result = sorted(result_dict.items(), key=lambda x: (x[1],x[0]))

for r,cnt in result:
    print(r)

