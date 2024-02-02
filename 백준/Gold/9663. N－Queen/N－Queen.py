from collections import deque
import copy

N = int(input())
visited = [0] * N
board = [0] * N

def dfs(depth):
    global count
    if depth == N:
        count += 1
        return
    
    for i in range(N):

        if visited[i] == 0:
            board[depth] = i

            if check(depth):
                visited[i] = 1
                dfs(depth + 1)
                visited[i] = 0

def check(n):
  for i in range(n):
    if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])):
      return False
  return True


count = 0
dfs(0)
print(count)