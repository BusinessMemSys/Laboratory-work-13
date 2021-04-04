k = [int(i) for i in input().split()]
a = list()
for i in range(len(k)):
    for j in range(len(k)):
        if k.index(k[i]) == k.index(k[j]):
            pass
        else:
            num = k[i]*int(k[j])
            a.append(num)
print("Ответ:", max(a))