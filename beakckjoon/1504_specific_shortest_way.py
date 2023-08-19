"""
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. 
(2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 
다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다.
(v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.
"""

import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
INF = int(1e10)
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())

def solution(start):
    distance = [INF for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0,start))
    while heap:
        dist, node = heapq.heappop(heap)
        if visited[node]:
            continue
        if dist > distance[node]:
            continue
        for next_node, next_dist in graph[node]:
            if distance[next_node] > distance[node] + next_dist:
                distance[next_node] = distance[node] + next_dist
                heapq.heappush(heap, (distance[next_node], next_node))
        visited[node] = True
    return distance

dist = solution(1)
dist_v1 = solution(v1)
dist_v2 = solution(v2)
            
path1 = dist[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist[v2] + dist_v2[v1] + dist_v1[N]

result = min(path1, path2, INF)
if result == INF:
    print(-1)
else:
    print(result)