c = list()
a = int(input('Введите целые неотрицательные числа '))
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
    c.append(a) 
    a = int(input())
else:
    print('Количество членов введенной последовательности ', c ,' равен ', len(c))
