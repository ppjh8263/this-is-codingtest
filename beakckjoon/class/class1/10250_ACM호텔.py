"""
2
6 12 10
30 50 72

402
1203
"""


import sys

input = sys.stdin.readline
T = int(input().rstrip())
inputs = []
for _ in range(T):
    inputs.append(map(int, input().split()))


for h, w, n in inputs:
    stair = n % h
    if stair == 0:
        stair = h
        num = n // h - 1
    else:
        num = n // h 
    print(f"{stair}{str(num  + 1).zfill(2)}")
    
