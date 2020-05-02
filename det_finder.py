lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

for i in range(len(lines)):
  lines[i] = lines[i].split(' ')
  for j in range(len(lines[i])):
    lines[i][j] = int(lines[i][j])

def determinant(a):
    if len(a) == 2 and len(a[0]) == 2:
        b = (a[0][0]*a[1][1]) - (a[0][1]*a[1][0])
        return b
    elif len(a) > 2:
        s = 0
        for i in range(len(a[0])):
            new_grid = remove_c_r(a, i, 0)
            sign = 1
            if i%2 != 0:
                sign = -1
            s += sign*a[0][i]*determinant(remove_c_r(a, i, 0))
        return s
    return 0

def remove_c_r(grid, c, r):
    temp = []
    for r in range(len(grid)):
        temp.append(grid[r])
    temp = temp[1:]
    for i in range(len(temp)):
        temp[i] = temp[i][:c] + temp[i][c+1:]
    return temp

print('Determinant:', determinant(lines))