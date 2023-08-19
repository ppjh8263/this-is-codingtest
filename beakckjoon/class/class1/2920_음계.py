import sys

input = sys.stdin.readline
N = list(map(int, input().split()))
is_ascending = True
is_descending = True
for n,i in zip(N, range(1, 9)):
    if n != i:
        is_ascending = False
        break

for n,i in zip(N, range(8, 0, -1)):
    if n != i:
        is_descending = False
        break

if is_ascending:
    print("ascending")
elif is_descending:
    print("descending")
else:
    print("mixed")