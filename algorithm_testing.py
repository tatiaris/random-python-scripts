n = int(input('Enter width: '))

lst = [1, 3, 6, 13]
while (len(lst) < n):
    lst.append(2*lst[-1] + ((len(lst) - 1) // 2)**((len(lst) + 1) % 2))

print(lst)

# 1, 3, 6, 13, 28, 60, 129
