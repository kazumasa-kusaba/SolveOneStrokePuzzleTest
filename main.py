from typing import List
import copy

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def isOnPuzzle(row_index: int, col_index: int, puzzle: List[List[int]]) -> bool:
  if row_index < 0 or len(puzzle) <= row_index:
    return False
  if col_index < 0 or len(puzzle[0]) <= col_index:
    return False
  return True

def isFilled(puzzle: List[List[int]]) -> bool:
  for row_index in range(len(puzzle)):
    for col_index in range(len(puzzle[0])):
      if puzzle[row_index][col_index] == 0:
        return False
  return True

def brute_force_sub(row_index: int, col_index: int, puzzle: List[List[int]], ans: List[tuple]) -> bool:
  if 2 <= puzzle[row_index][col_index]:
    return False
  
  if isFilled(puzzle):
    return True
  
  for direction in directions:
    before_row_index, before_col_index = row_index, col_index
    row_index, col_index = row_index + direction[0], col_index + direction[1]
    if isOnPuzzle(row_index, col_index, puzzle):
      puzzle[row_index][col_index] += 1
      ans.append((col_index, row_index))
      if brute_force_sub(row_index, col_index, puzzle, ans):
        return True
      puzzle[row_index][col_index] -= 1
      ans.pop()
    row_index, col_index = before_row_index, before_col_index
  
  return False

def brute_force(puzzle: List[List[int]], ans: List[tuple]) -> bool:
  checked = copy.deepcopy(puzzle)
  for row_index in range(len(puzzle)):
    for col_index in range(len(puzzle[0])):
      if checked[row_index][col_index] == 0:
        checked[row_index][col_index] == 1
        ans.append((col_index, row_index))
        if brute_force_sub(row_index, col_index, puzzle, ans):
          return True
        ans.pop()
  return False

if __name__ == '__main__':
  ans = []

  # puzzle
  # 0: route
  # 1: obstacle or the place user took
  puzzle = [[1, 1, 0, 0, 0],\
            [1, 1, 1, 1, 0],\
            [0, 0, 0, 1, 0],\
            [0, 0, 0, 0, 0],\
            [0, 0, 0, 0, 0]]
  
  for row_index in range(len(puzzle)):
    for col_index in range(len(puzzle[0])):
      print(str(puzzle[row_index][col_index]) + " ", end="")
    print()

  ret = brute_force(puzzle, ans)
  if ret:
    print("This puzzle can be solved. The route is below.")
    print(ans)
  else:
    print("This puzzle cannot be solved.")

