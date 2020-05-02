from fractions import Fraction
import math

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
inp_grid = text.split('\n')

for i in range(len(inp_grid)):
  inp_grid[i] = inp_grid[i].split(' ')
  for j in range(len(inp_grid[i])):
    inp_grid[i][j] = int(inp_grid[i][j])

def get_row_list(grid):
  list = grid.split('\n')
  list = list[:-1]
  return list

def solve_matrix(grid):
  print('\n')
  try:    
    for i in range(len(grid)):
      for m in range(len(grid[i])-1, -1, -1):
        grid[i][m] /= grid[i][i]
      for j in range(i+1, len(grid)):
        lcm = grid[j][i]/grid[i][i]
        for k in range(len(grid[j])):
          grid[j][k] -= lcm*grid[i][k]
      # printing the grid to show steps of solving
      for row in grid:
        print(row)
      print('~')

    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] % 1 < 0.001 or grid[i][j] % 1 > 0.998:
          grid[i][j] = round(grid[i][j])
    # printing the final matrix in raw echelon form
    for row in grid:
      print(row)
    print('\n')
    # at this point we have the final matrix
    xn = grid[len(grid)-1][len(grid[0])-1]/grid[len(grid)-1][len(grid[0])-2]
    if xn%1 < 0.001 or xn%1 > 0.998:
        print('n' + str(i+1) + ' = ' + str(round(xn)))
    else:
      frac = Fraction(xn)
      print('n' + str(i+1) + ' = ' + str(frac))

    for i in range(len(grid)-1):
      grid[i][len(grid[i])-2] *= xn
    for i in range(len(grid)-2, -1, -1):
      x = grid[i][len(grid[i]) - 1]
      for j in range(i+1, len(grid[i])-1):
        x -= grid[i][j]
      for k in range(i):
          grid[k][i] *= x
      if x%1 < 0.001 or x%1 > 0.998:
        print('x' + str(i+1) + ' = ' + str(round(x)))
      else:
        frac = Fraction(x)
        print('x' + str(i+1) + ' = ' + str(frac))
    return grid
  except Exception:
    print('\nno unique solution')

solve_matrix(inp_grid)

# def multiply_matrices(m1, m2):
#   if len(m1) != len(m2[0]):
#     print('not possible')
#   else:
#     m_final = []
#     for y in range(size):
#       grid = grid + [[]]
#       for x in range(size):
#           grid[y] = grid[y] + [0]
#     for row in range():
#       for i in range(len(m1)):
#         m[i] = []
#         for j in range(len(m2[i])):
#           m_final[i][j]