# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

with open ('file.txt', 'r') as f:
    positions = f.read().split('\n')
positions = list(map(int, positions))

N = int(input("Введите число: "))
spam = list(range(-N, N+1))
print(spam)
prod = 1
for x in positions:
    i = int(x)
    prod = prod * spam[i]
print(prod)

