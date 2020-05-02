from math import sqrt

r = 0.082057
def mol_speed(t, m):
    return sqrt(8*r*t/(3.142*m))

def van_der_waal(n, v, a, b, t):
    return (n*r*t)/(v-n*b) - ((n**2)*a)/(v**2)

def density(p, m, t):
    return (p*m)/(r*t)
def percent_diff(pe, pc):
    pi = (pe-pc)/((pe+pc)/2)
    pi *= 100
    return pi
print(van_der_waal(10.05, .8216, 2.253, 4.278*(10**-2), 303.8))
# print(percent_diff(12.23, van_der_waal(1.057, 1.943, 1.36, 3.183*(10**-2), 274)))