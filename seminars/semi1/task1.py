#  Вывсти квадрат числа.


#a = int(input())
#print(a**2)


# Напишите программу, которая принимает два числа на вход и проверяет, является ли одно число квадратом другого

# a = int(input())
# b = int(input())

# if a == b**2 or b == a**2:
#     print(f'Является')
# else:
#     print(f'Не является')



a = int(input())
max = a
for i in range(4):
    b=int(input())
    if b > max:
        max = b
print(max)

