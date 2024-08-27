import sys

input = sys.stdin.readline

alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
count = list(map(int, '3 2 1 2 4 3 1 3 1 1 3 1 3 2 1 2 2 2 1 2 1 1 1 2 2 1'.split()))

alpha_count = {}

for a, c in zip(alpha, count):
  alpha_count[a] = c

N, M = map(int, input().split());

name1, name2 = input().rstrip().split();

name = []

for i in range(min(N, M)):
  name += name1[i];
  name += name2[i];

name += name1[min(N, M):]
name += name2[min(N, M):]


name_value = [ alpha_count[i] for i in name ]
while len(name_value) > 2:
  new_name_value = []

  for i in range(len(name_value) - 1): 
    new_name_value.append((name_value[i] + name_value[i + 1]) % 10)

  name_value = new_name_value

num1, num2 = name_value

print(str(10*num1 + num2) + '%')