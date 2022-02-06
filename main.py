from typing import List
import copy

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def isFilled(maze: List[List[int]]) -> bool:
  for row_index in range(len(maze)):
    for col_index in range(len(maze[0])):
      if maze[row_index][col_index] == 0:
        return False
  return True

def brute_force_sub(row_index: int, col_index: int, maze: List[List[int]], ans: List[tuple]) -> bool:
  if row_index < 0 or len(maze) <= row_index:
    return False
  if col_index < 0 or len(maze[0]) <= col_index:
    return False
  if maze[row_index][col_index] == 1:
    return False

  maze[row_index][col_index] = 1
  
  if isFilled(maze):
    return True
  
  for direction in directions:
    before_row_index, before_col_index = row_index, col_index
    row_index += direction[0]
    col_index += direction[1]
    ans.append((col_index, row_index))
    if brute_force_sub(row_index, col_index, maze, ans):
      return True
    ans.pop()
    row_index, col_index = before_row_index, before_col_index
  
  return False

def brute_force(maze: List[List[int]], ans: List[tuple]) -> bool:
  checked = copy.deepcopy(maze)
  for row_index in range(len(maze)):
    for col_index in range(len(maze[0])):
      if checked[row_index][col_index] == 0:
        checked[row_index][col_index] == 1
        ans.append((col_index, row_index))
        if brute_force_sub(row_index, col_index, maze, ans):
          return True
        ans.pop()
  return False

if __name__ == '__main__':
  ans = []

  # maze
  # 0: route
  # 1: obstacle or the place user took
  maze = [[1, 1, 0, 0, 0],\
          [1, 1, 1, 1, 0],\
          [0, 0, 0, 1, 0],\
          [0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0]]
  
  for row_index in range(len(maze)):
    for col_index in range(len(maze[0])):
      print(str(maze[row_index][col_index]) + " ", end="")
    print()

  ret = brute_force(maze, ans)
  if ret:
    print("This maze can be solved. The route is below.")
    print(ans)
  else:
    print("This maze can not be solved.")

