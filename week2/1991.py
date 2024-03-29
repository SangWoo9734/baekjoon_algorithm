import sys

input = sys.stdin.readline

N = int(input())

vertex = [ list(input()[:-1].split(' ')) for _ in range(N) ]

stack = []
graph = {}

for v in vertex:
    n, l, r = v
    graph[n] = {
        'left': l if l != '.' else None,
        'right': r if r != '.' else None,
    }

def pre_cycle(letter):
    print(letter, end='')
    if graph[letter]['left']:
        pre_cycle(graph[letter]['left'])
    if graph[letter]['right']:
        pre_cycle(graph[letter]['right'])

def mid_cycle(letter):
    if graph[letter]['left']:
        mid_cycle(graph[letter]['left'])
    print(letter, end='')
    if graph[letter]['right']:
        mid_cycle(graph[letter]['right'])

def post_cycle(letter):
    if graph[letter]['left']:
        post_cycle(graph[letter]['left'])
    if graph[letter]['right']:
        post_cycle(graph[letter]['right'])
    print(letter, end='')

pre_cycle('A')
print()
mid_cycle('A')
print()
post_cycle('A')
print()