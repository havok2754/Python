# Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  


from math import pi

d = str(input("Введите число для заданной точности числа Пи:\n"))
x = len(d) - 2
print(f'число Пи с заданной точностью {d} равно {round(pi, x)}')