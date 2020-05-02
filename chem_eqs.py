from chem import *

def heat_flow(n, phase_change):
    return n*phase_change

def enthalpy_change_reaction(vp, hp, vr, hr):
    h = 0
    for i in range(len(vp)):
        h += vp[i]*hp[i]
    for i in range(len(vr)):
        h -= vr[i]*hr[i]
    return h

def total_h(list_h):
    return sum(list_h)
