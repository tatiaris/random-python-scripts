import time
from math import factorial

def print_grid(g):
    for r in g:
        print(r)
    print()

def to_tuple(g):
    return tuple([tuple(r) for r in g])

def get_grid(k):
    m = [['']*len(k[i]) for i in range(3)]
    for i in range(len(k)):
        for j in range(len(k[i])):
            m[i][j] = k[i][j]
    return m

def can_insert_element(g, i, j, s):
    if (g[i][j] != '' or i + s - 1 >= len(g) or j + s - 1 >= len(g[i])):
        return False
    for m in range(s):
        for n in range(s):
            if (g[i + m][j + n] != ''):
                return False
    return True

def insert_element(g, i, j, s, e):
    for m in range(s):
        for n in range(s):
            g[i + m][j + n] = e
    return to_tuple(g)

def is_full(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if (g[i][j] == ''):
                return False
    return True

def x_flip(g):
    temp = [['']*len(g[0]) for i in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            temp[i][len(temp[i]) - j - 1] = g[i][j]
            temp[i][j] = g[i][len(g[i]) - j - 1]
    return to_tuple(temp)

def y_flip(g):
    temp = [['']*len(g[0]) for i in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            temp[len(temp) - i - 1][j] = g[i][j]
            temp[i][j] = g[len(g) - i - 1][j]
    return to_tuple(temp)

def fill_humans(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if (g[i][j] == ''):
                g[i][j] = 'h'
    return to_tuple(g)

def add_unit(g):
    global g_list, unique_gs

    if (g in unique_gs):
        return 0

    if (is_full(g)):
        g_list.update([g, y_flip(g), x_flip(g), x_flip(y_flip(g))])
        unique_gs.update([g, y_flip(g), x_flip(g), x_flip(y_flip(g))])
        return 1

    unique_gs.update([g, y_flip(g), x_flip(g), x_flip(y_flip(g))])

    for i in range(len(g)):
        for j in range(len(g[i])):
            if (can_insert_element(g, i, j, 3)):
                add_unit(insert_element(get_grid(g), i, j, 3, army[3]))
            else:
                add_unit(fill_humans(get_grid(g)))


# l = int(input('Enter length: '))
l = 3
w = int(input('Enter width: '))

start_time = time.time()

grid = to_tuple([['']*w for i in range(l)])

army = {3:'m', 2:'g', 1:'h'}
g_list = set()
unique_gs = set()
add_unit(grid)

for g in g_list:
    print_grid(g)

print('possible combinations:', len(set(g_list)))
# print('possible combinations M:', len(set(g_list)) - 1)
# print('unknown:', len(set(g_list)) - 1 - 2*(w - 1) - 4*sum(list(range(w - 2))))
print('time taken:', time.time() - start_time, 'seconds')
