<<<<<<< HEAD
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

print('Введите вещественное число')
a = float(input())

=======
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

print('Введите вещественное число')
a = float(input())

>>>>>>> 38d518edd7576fa256c250883a17b84c37e7a701
print(int(a * 10) % 10)