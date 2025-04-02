import heapq
import sys

input = sys.stdin.readline

INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    edges.append((u, v, w))

# 모든 정점에서 다익스트라 수행
dist = [[INF] * N for _ in range(N)]
count = [[0] * N for _ in range(N)]

for start in range(N):
    dist[start][start] = 0
    count[start][start] = 1
    hq = [(0, start)]

    while hq:
        cost, cur = heapq.heappop(hq)

        if cost > dist[start][cur]:
            continue

        for to, w in graph[cur]:
            new_cost = cost + w
            if new_cost < dist[start][to]:
                dist[start][to] = new_cost
                count[start][to] = count[start][cur]
                heapq.heappush(hq, (new_cost, to))
            elif new_cost == dist[start][to]:
                count[start][to] += count[start][cur]

# 각 간선이 몇 개의 최단 경로에 "필수적으로 포함되는지" 계산
# 즉, 해당 간선을 제거했을 때 최단 경로가 늘어나는 경우만 카운트
result = []
for u, v, w in edges:
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if dist[i][j] == INF:
                continue
            # 간선 (u, v) 없이 경로가 안 된다면 필수
            # 즉, 이 간선을 포함한 경로가 아니면 최단거리가 될 수 없음
            cond1 = dist[i][j] == dist[i][u] + w + dist[v][j] and count[i][j] == count[i][u] * count[v][j]
            cond2 = dist[i][j] == dist[i][v] + w + dist[u][j] and count[i][j] == count[i][v] * count[u][j]
            if cond1 or cond2:
                cnt += 1
    result.append(cnt)

print(*result)


## 플루이드 워셜

import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    row = [float('inf')] * N
    row[i] = 0
    graph.append(row)

cost_input = []
for _ in range(M):
    f, t, time = map(int, input().split())
    cost_input.append([f, t, time])
    graph[f][t] = time
    graph[t][f] = time

def minimum_cost_graph(graph):
    new_graph = copy.deepcopy(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if new_graph[i][j] > new_graph[i][k] + new_graph[k][j]:
                    new_graph[i][j] = new_graph[i][k] + new_graph[k][j]
    return new_graph

origin_cost = minimum_cost_graph(graph)
result = [0] * M

for idx, (f, t, time) in enumerate(cost_input):
    # 간선 제거
    graph[f][t] = float('inf')
    graph[t][f] = float('inf')

    parade_cost = minimum_cost_graph(graph)

    for i in range(N):
        for j in range(i + 1, N):
            if origin_cost[i][j] < parade_cost[i][j] or parade_cost[i][j] == float('inf'):
                result[idx] += 1

    # 간선 복원
    graph[f][t] = time
    graph[t][f] = time

print(*result)