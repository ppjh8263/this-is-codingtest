from copy import deepcopy
import queue
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


result = -1
virus_quque = deque()
walls = []


def check_xy(r, c):
    if r < 0 or c < 0 or r >= N or c >= M:
        return False
    return True


def virus(_arr):
    global result
    for r in range(N):
        for c in range(M):
            if _arr[r][c] == 2:
                virus_quque.append((r,c))

    while virus_quque:
        r, c = virus_quque.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            y, x = r + dy, c + dx
            if not check_xy(y, x):
                continue
            if _arr[y][x] == 0:          
                _arr[y][x] = 2
                if (y,x) not in virus_quque:
                    virus_quque.append((y,x))

    tmp_result = 0
    for a in _arr:
        tmp_result += a.count(0)

    result = max(result,tmp_result)


def set_wall():
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                walls.append((r,c))

    return combinations(range(len(walls)),3)


for w1, w2, w3 in set_wall():
    _arr = deepcopy(arr)
    (y1,x1),(y2,x2),(y3,x3) = walls[w1],walls[w2],walls[w3]
    _arr[y1][x1] = 1
    _arr[y2][x2] = 1
    _arr[y3][x3] = 1
    virus(_arr)

print(result)
