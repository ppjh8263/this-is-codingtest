import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
target_n = 666
cnt = 0
while True:
    if "666" in str(target_n):
        cnt += 1
    if cnt == N:
        print(target_n)
        break
    target_n += 1