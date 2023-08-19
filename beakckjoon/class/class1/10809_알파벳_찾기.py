import sys

input = lambda : sys.stdin.readline().rstrip()
start_n = ord('a')
end_n = ord('z')
first_loc = [-1 for _ in range(end_n - start_n + 1)]

S = input()

for i, s in enumerate(S):
    idx = ord(s) - start_n
    if first_loc[idx] == -1:
        first_loc[idx] = i
    else:
        continue

print(' '.join(map(str, first_loc)))
