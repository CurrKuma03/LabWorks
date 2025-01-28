import math

X = float(input("Введите значение A: "))
Y = float(input("Введите значение B: "))
Z = float(input("Введите значение x: "))

result1 = math.log (Y ** (-math.sqrt(abs(X))))
result2 = X - (Y/2)
result3 = (math.sin(math.atan(Z))) ** 2

M = result1 * result2 + result3
print ('Результат: ', M )
