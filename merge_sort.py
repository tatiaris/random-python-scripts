from random import random
import time

def merge_sort(lst):
    if (len(lst) == 1):
        return lst
    mid = len(lst)//2
    merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))

def merge(l1, l2):
    l3 =  []
    k = len(l1) + len(l2)
    for i in range(k):
        if (len(l1) > 0 and len(l2) > 0):
            if (l1[0] < l2[0]):
                l3.append(l1.pop(0))
            else:
                l3.append(l2.pop(0))
        elif (len(l1) > 0):
            l3.append(l1.pop(0))
        else:
            l3.append(l2.pop(0))
    return l3

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

t = int(input('enter number of elements: '))
start_time = time.time()
mergeSort([random() for i in range(t)])
print('\nsorting', t, 'elements using mergeSort')
print('time taken:', time.time() - start_time, 'seconds\n')

start_time = time.time()
merge_sort([random() for i in range(t)])
print('sorting', t, 'elements using merge_sort')
print('time taken:', time.time() - start_time, 'seconds\n')
