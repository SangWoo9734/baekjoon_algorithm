import sys

input = sys.stdin.readline

N = int(input())

nums = [ int(input()) for _ in range( N ) ]

m_nums = max(nums)


dp = [  [], [ 1, 0, 0 ], [ 0, 1, 0 ], [ 1, 1, 1 ] ] + [ [ 0, 0, 0 ] for _ in range( m_nums - 3 ) ] 

for j in range(4, m_nums + 1):
  dp[j][0] = (dp[j - 1][1] + dp[j - 1][2]) % 1000000009
  dp[j][1] = (dp[j - 2][0] + dp[j - 2][2]) % 1000000009
  dp[j][2] = (dp[j - 3][0] + dp[j - 3][1]) % 1000000009

for n in nums:
  print(sum(dp[n]) % 1000000009)





  


# 1 : [ 1 ] 1

# 2 : [ 2 ] 1

# 3 : [ 1, 2 ], [ 2, 1 ], [ 3 ] 3

# 4 : [ 1, 2, 1 ], [ 3 , 1 ], [ 1, 3 ] 3

# 5 : [ 2, 1, 2 ], [ 3. 2 ], [ 2, 3 ], [ 1, 3, 1 ]

# 6 : [ 1, 2, 3 ], [ 1, 3, 2 ], [ 2, 1, 3 ], [ 2, 3, 1 ], [ 3, 1, 2 ], [ 3, 2, 1 ]