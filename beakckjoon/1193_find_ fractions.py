from math import comb
import sys
input = sys.stdin.readline
X = int(input())


for i in range(1, 10000001):
    X -= i
    if X <= 0:
        if i % 2 == 0:
            r = 1
            c = i
            r = r + (X + i) - 1
            c = c - (X + i) + 1
            break
        else:
            r = i
            c = 1
            r = r - (X + i) + 1
            c = c + (X + i) - 1
            break
print(f"{r}/{c}")
