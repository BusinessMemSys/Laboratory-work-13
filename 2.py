from random import randint  #импортируем модуль random

arr = []                    #пустой список
for i in range(10):         #цикл for для заполнения списка
    a = randint(10, 100)
    arr.append(a)
print("Список: ",arr)
k = 1
max_sum = arr[k] / arr[k + 1]   
for i in range(3, 10):
    if arr[i - 1] / arr[i] > max_sum:
        max_sum = arr[i - 1] / arr[i]
        k = i - 1
print('Решение: {} / {} = {} '.format(arr[k], arr[k + 1], max_sum)) 
print('Ответ: {} '.format(max_sum)) 