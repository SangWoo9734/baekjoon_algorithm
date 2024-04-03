import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(y, x):
    if 0 > x or x >= N or 0 > y or y >= N or apart[y][x] != 1:
        return 0

    apart[y][x] = '0'
    count = 1  # 각각의 dfs 호출마다 count 값이 1로 초기화됩니다.

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        count += dfs(ny, nx)  # dfs 호출 시 count 값을 누적합니다.

    return count

N = int(input())
apart = [list(map(int, input()[:-1])) for _ in range(N)]

apart_count = []

for i in range(N):
    for j in range(N):
        if apart[i][j] == 1:
            count = dfs(i, j)
            apart_count.append(count)

print(len(apart_count))
print(*sorted(apart_count), sep='\n')
