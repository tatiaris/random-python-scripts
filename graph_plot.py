from statistics import mean, stdev
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) / ((mean(xs)*mean(xs)) - mean(xs*xs)))
    b = mean(ys) - m*mean(xs)
    return m, b

def determine_bool(s):
    if s == 'y':
        return True
    return False

def rsquared(x, y):
    """ Return R^2 where x and y are array-like."""

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return r_value**2

file_name = input('Enter file name: ')
while file_name[-1] == ' ':
    file_name = file_name[:-1]
while file_name[0] == ' ':
    file_name = file_name[1:]
xn = int(input('Enter x-index: '))
yn = int(input('Ente y-index: '))
b_best_fit = determine_bool(input('Best fit line (enter \'y\' or \'n\'): '))
b_min_max = determine_bool(input('Min - Max wanted (enter \'y\' or \'n\'): '))
lab_data = open(file_name, 'r').read().split('\n')
while lab_data[-1] == '':
    lab_data.pop(-1)
titles = lab_data.pop(0).split(',')
x_values = []
y_values_raw = []
y_values = []
std_so_far = []

n = 0
for i in range(len(lab_data)):
# for i in range(1, 21):
    lab_data[n] = list(map(float, lab_data[n].split(',')))
    y_values.append(lab_data[n][yn])
    # x_values.append(lab_data[i][xn])
    x_values.append(n)
    # y_values.append(sum(y_values_raw)/i)
    # if (i > 1):
    #     std_so_far.append(stdev(y_values))
    n += 1

y_max = max(y_values)
x_max_ind = y_values.index(y_max)
y_min = min(y_values)
x_min_ind = x_values[y_values.index(y_min)]
dy = y_max-y_min
x_mid = (max(x_values) + min(x_values))/2
y_mid = (y_max + y_min)/2
ind_x = abs(max(x_values) - min(x_values))/4
ind_y = (y_max-y_min)/3
r_2 = rsquared(x_values, y_values)
x_values = np.array(x_values)
y_values = np.array(y_values)
m, b = best_fit_slope_and_intercept(x_values, y_values)
bf_eq = 'y = ' + str(round(b, 3)) + ' + ' + str(round(m, 3)) + 'x'

plt.plot(x_values, y_values, '.')
plt.xlabel(titles[xn])
plt.ylabel(titles[yn])
plt.title(titles[xn] + ' vs ' + titles[yn])
plt.grid(True)

if b_best_fit:
    plt.plot(np.unique(x_values), np.poly1d(np.polyfit(x_values, y_values, 1))(np.unique(x_values)))
    # plt.annotate(bf_eq + '\nr^2 = ' + str(r_2), xy = (max(x_values)-1.5*ind_x, y_max), xytext = (max(x_values)-1.5*ind_x, y_max), arrowprops = dict(facecolor='black', shrink=0.05))
if b_min_max:
    plt.annotate('Max (' + str(x_max_ind) + ', ' + str(round(y_max, 3)) + ')', xy = (x_max_ind, y_max), xytext = (x_max_ind, y_max - ind_y), arrowprops = dict(facecolor='black', shrink=0.05))
    plt.annotate('Min (' + str(x_min_ind) + ', ' + str(round(y_min, 3)) + ')', xy = (x_min_ind, y_min), xytext = (x_min_ind - ind_x, y_min + ind_y), arrowprops = dict(facecolor='black', shrink=0.05))
    plt.annotate('ΔT = ' + str(round(dy, 3)) + ' C', xy = (x_mid, y_mid), xytext = (x_mid, y_mid), arrowprops = dict(facecolor='black', shrink=0.05))

plt.show()
