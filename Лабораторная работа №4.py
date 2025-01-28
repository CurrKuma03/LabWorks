a = 1
r = 0
result2 = 0
n = int(input('Сколько членов в последовательности? '))
while r < n:
    r += 1
    result = a ** 3
    a += 1
    result2 += result
else: 
    print('Сумма кубов из ', n ,'членов равен', result2)
