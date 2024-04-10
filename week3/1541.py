import sys

input = sys.stdin.readline

S = input().rstrip()

minus_arr = S.split('-')

sub_res = []

for i in minus_arr:
  sub_res.append(sum(map(int, i.split('+'))))

ans = sub_res[0]

for i in sub_res[1:]:
  ans -= i

print(ans)