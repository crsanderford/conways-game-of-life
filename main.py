import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def neighborhood(cell): #returns adjacent cells
  x, y = cell
  return [(x - 1, y - 1), (x    , y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x    , y + 1), (x + 1, y + 1)]


def apply_iteration(board): #returns the subsequent board state
  new_board = set([])

  neighbors = board.union(set(n for cell in board for n in neighborhood(cell))) #generate a set of all cells which are live or are adjacent to live cells

  for cell in neighbors: #count live cells adjacent to every cell in neighbors, then add the cell to the subsequent board state if it satisfies the rules
    neighborcount = sum((n in board) for n in neighborhood(cell))
    if neighborcount == 3 or (neighborcount == 2 and cell in board):
      new_board.add(cell)
  return new_board
boards = []
board = {(0,1), (1,2), (2,0), (2,1), (2,2)}
iterationcount = 10
for _ in range(iterationcount):
  board = apply_iteration(board)
  print(board)
  boards.append(board)

iter = 0

for stuff in boards:
  exes = []
  whys = []
  iter = iter + 1
  for n in stuff:
    exes.append(list(n)[0])
    whys.append(list(n)[1])
  plt.scatter(exes,whys)
  plt.savefig('plot' + str(iter) + '.png')
  plt.clf()
    

