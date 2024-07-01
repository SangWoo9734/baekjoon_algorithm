import sys

import re

input = sys.stdin.readline

n = int(input())

target = input().rstrip()

res = re.sub(r'[a-zA-Z]+',  ' ', target)

print(sum(map(int, res.split())))