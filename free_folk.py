import time
from math import factorial

def print_grid(g):
    for r in g:
        print(r)
    print()

def to_tuple(g):
    return tuple([tuple(r) for r in g])

def flip(g):
    temp = [['']*len(g[0]) for i in range(len(g))]
    temp2 = [['']*len(g[0]) for i in range(len(g))]
    temp3 = [['']*len(g[0]) for i in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            temp[i][j] = g[i][len(g[i]) - j - 1]
            temp2[i][j] = g[len(g) - i - 1][j]
            temp3[i][j] = g[len(g) - i - 1][len(g[0]) - j - 1]

    return [to_tuple(temp), to_tuple(temp2), to_tuple(temp3)]

def add_unit(g):
    global g_list, unique_gs

    if (g in unique_gs):
        return 0

    if (is_full(g)):
        g_list.update([g] + flip(g))
        unique_gs.update([g] + flip(g))
        return 1

    unique_gs.update([g] + flip(g))

    for i in range(len(g)):
        for j in range(len(g[i])):
            add_unit(insert_element(get_grid(g), 3, army[3]))
            add_unit(insert_element(get_grid(g), 2, army[2]))
            add_unit(insert_element(get_grid(g), 1, army[1]))

# l = int(input('Enter length: '))
l = 3
w = int(input('Enter width: '))

start_time = time.time()

grid = to_tuple([['']*w for i in range(l)])

army = {3:'m', 2:'g', 1:'h'}
g_list = set()
unique_gs = set()

get_combos(grid)

print('possible combinations:', len(set(g_list)))
print('time taken:', time.time() - start_time, 'seconds')

# 1, 3, 6, 13, 28, 60
