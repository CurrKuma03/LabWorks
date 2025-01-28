a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if a < b:
    if a < c:
        result = a
    else:
        result = c
elif b < a:
    if b < c:
        result = b
    else:
        result = c
print ('Минимальное из этих чисел: ', result)