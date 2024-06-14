import sys

input = sys.stdin.readline

a, b = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_B = len(set(A) - set(B))
B_A = len(set(B) - set(A))
print(A_B + B_A)