import sys

input = sys.stdin.readline
N = int(input().rstrip())
INF = int(1e10)
b_offset = N + 1

gragh = {
    "A" : [[] for _ in range(N + 1)],
    "B" : [[] for _ in range(N + 1)]
    }
pre_atob, pre_btoa = 0, 0
for i in range(N - 1):
    a, b, atob, btoa = map(int, input().split())
    gragh["A"][i].append(("A", i + 1, a))
    gragh["A"][i].append(("B", i + 1, b + pre_atob))
    gragh["B"][i].append(("B", i + 1, b))
    gragh["B"][i].append(("A", i + 1, a + pre_btoa))
    pre_atob, pre_btoa = atob, btoa 
a,b = map(int, input().split())
gragh["A"][N - 1].append(("A", N, a))
gragh["A"][N - 1].append(("B", N, b + pre_atob))
gragh["B"][N - 1].append(("B", N, b))
gragh["B"][N - 1].append(("A", N, a + pre_btoa))

import heapq

def solution(start):
    distance = {
        "A" : [INF for _ in range(N + 1)],
        "B" : [INF for _ in range(N + 1)]
    }
    heap = []
    distance[start][0] = 0
    heapq.heappush(heap, (0, start, 0))
    
    while heap:
        dist, place, node = heapq.heappop(heap)
        if distance[place][node] < dist:
            continue
        for next_place, next_node, next_dist in gragh[place][node]:
            cost = distance[place][node] + next_dist
            if distance[next_place][next_node] > cost:
                distance[next_place][next_node] = cost
                heapq.heappush(heap,(cost, next_place, next_node))
    
    return distance

start_a = solution("A")
start_b = solution("B")
print(min(start_a["A"][-1],start_a["B"][-1],start_b["A"][-1],start_b["B"][-1]))




