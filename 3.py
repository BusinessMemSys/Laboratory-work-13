import math    #импортируем модуль math
k = list(int(i) for i in input().split())  #генератор списка
lst = []
lst1 = []
lst2 = []
if len(k)%2 != 0:   #если кол-во элементов нечетное, добавляем 0 в список
    k.append(0)
for i in range(0, len(k)-1, 2):
    ls = [k[i], k[i+1]]
    lst.append(ls)
for i in range(len(ls)//2):
    w = math.sqrt(((lst[i][0]-lst[i+1][0])**2)+(((lst[i][1]-lst[i+1][1]))**2))
    lst1 = [ls[i]]
    lst2 = [w]
a, b = lst2.index(max(lst2)), lst2.index(min(lst2))
c, d = a+1, b+1
print("Расстояние между точками {0}см".format(sum(lst2)))
print("Минимальное расстояние между точка с координатами",lst[b],"и", lst[d])
print("Наибольшее расстояние между точка с координатами",lst[a],"и", lst[c])