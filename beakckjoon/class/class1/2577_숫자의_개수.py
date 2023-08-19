import sys
from collections import Counter
input = sys.stdin.readline
A = int(input().rstrip())
B = int(input().rstrip())
C = int(input().rstrip())

N = str(A * B * C)
count_n = Counter(N)

for i in range(10):
    if str(i) not in count_n:
        print(0)
    else:
        print(count_n[str(i)])




