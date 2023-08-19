"""
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4
"""
import sys
input = sys.stdin.readline
from collections import deque

N, num_party = map(int, input().split())
knowings = list(map(int, input().split()))
party = deque()
for _ in range(num_party):
    party.append(set(list(map(int, input().split()))[1:]))


pass_cnt = 0

if knowings[0] != 0:
    target = set(knowings[1:])
    while len(party) != pass_cnt:
        p = party.popleft()
        if len(list(target & p)) != 0:
            for a in p:
                target.add(a)
            pass_cnt = 0
            num_party -= 1
        else:
            pass_cnt += 1
            party.append(p)

            
print(num_party)
