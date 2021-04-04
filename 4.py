n, m = map(int, input().split())
matrix =[list(map(int, input().split())) for _ in range(n)]
print()
for row in list(zip(*matrix)):  #zip функция объединяет список, 
        print(*row)             #оператор * распаковывает список 