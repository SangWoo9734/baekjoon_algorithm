import sys
from itertools import combinations

def team_power(board, team):
  combi = list(combinations(team, 2))

  total_opp = 0

  for c in combi:
    i, j = c
    total_opp += board[i][j] + board[j][i]

  return total_opp


input = sys.stdin.readline

N = int(input())

board = [ list(map(int, input().split())) for _ in range(N) ]

vs_team = list(combinations(range(N), N//2))

min_gap = sys.maxsize

for team_1 in vs_team:
  team_2 = list(filter(lambda x: not x in team_1, range(N)))

  team_power_1 = team_power(board, team_1)
  team_power_2 = team_power(board, team_2)

  gap = abs(team_power_1 - team_power_2)

  if gap == 0:
    min_gap = 0
    break

  min_gap = min_gap if min_gap < gap else gap

print(min_gap)