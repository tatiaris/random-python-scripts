from tkinter import *
from tkinter.scrolledtext import ScrolledText
from fractions import Fraction
import math

root = Tk()
root.title("Matrix Solver")
root.geometry("680x150+700+100")
Label(root, text="Matrice: ").grid(row=1, column=0)
user_input = ScrolledText(root, height=4); user_input.grid(row=1, column=1)

def get_row_list(grid):
  list = grid.split('\n')
  list = list[:-1]
  return list

def solve_matrix():
  print('\n')
  try:
    grid = []
    rows = get_row_list(user_input.get(1.0, END))
    for l in rows:
      grid.append(l.split(' '))
    for rows in grid:
      for num in rows:
        if num == '':
          print('\ninvalid grid')
          return 0
        try:
          if int(num):
            continue
        except Exception:
          print('\ninvalid grid')
          return 0
    if not len(grid) == (len(grid[0]) - 1):
      print('\nplease enter a square matrix (excluding equals column)')
      return Exception
    for i in range(len(grid)):
      grid[i] = list(map(int, grid[i]))
    for i in range(len(grid)):
      for m in range(len(grid[i])-1, -1, -1):
        grid[i][m] /= grid[i][i]
      for j in range(i+1, len(grid)):
        lcm = grid[j][i]/grid[i][i]
        for k in range(len(grid[j])):
          grid[j][k] -= lcm*grid[i][k]
      # print(grid)
      for row in grid:
        print(row)
      print('\n')

    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] % 1 < 0.001 or grid[i][j] % 1 > 0.998:
          grid[i][j] = round(grid[i][j])

    for row in grid:
      print(row)
    # at this point we have the final matrix

    xn = grid[len(grid)-1][len(grid[0])-1]/grid[len(grid)-1][len(grid[0])-2]
    print('x' + str(len(grid[0]) - 1) + ' = ' + str(xn))
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
    print('\ngrid impossible to solve')

submit = Button(root, text = "Submit", width = 30, height = 2, bg = 'lightblue', command = solve_matrix).place(x = 200, y = 90)
root.mainloop()



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