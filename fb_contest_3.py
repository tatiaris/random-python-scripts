t = int(input())
t1 = 1
while t1 <= t:
    s=input()
    if s.count(s[0]) == 1:
        print("Case #"+str(t1)+": Impossible")
    else:
        a = s
        flag = 0
        b = ''
        for k in range(s.__len__()):
            b = s[0:k] + s
            res = 'true'
            i, j = 0, 0
            while(j <= b.__len__()):

                if i >= a.__len__():
                    res = 'true'
                    break

                if j >= b.__len__():
                    res = 'false'
                    break

                if a[i] == b[j]:
                    i += 1
                    j += 1
                    continue

                if i == 0:
                    j += 1
                    continue
                i = 0

            if res == 'false':
                flag = 1
                break
        if flag == 0:
            print("Case #" + str(t1) + ": Impossible")
        else:
            print("Case #" + str(t1) + ": " + b)

    t1+=1
