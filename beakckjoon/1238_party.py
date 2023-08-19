from dis import dis
import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
INF = int(1e10)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def solution(start):
    distance = [INF for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        dist, node = heapq.heappop(heap)
        if visited[node]:
            continue
        if dist > distance[node]:
            continue
        for next_node, next_dist in graph[node]:
            cost = distance[node] + next_dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
        visited[node] = True
    
    return distance

dist_dict = {}
dist_dict[X] = solution(X)
result = -1
for n in range(1,N+1):
    if n not in dist_dict:
        dist_dict[n] = solution(n)
    tmp_cost = dist_dict[n][X] + dist_dict[X][n]
    if tmp_cost > result:
        result = tmp_cost

print(result)