# 3'. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# Пример :
# абвгдабвгд -> 2
# абв

a = input()
b = input()
if len(a)>len(b):
    print(a.count(b))
else:
    print(b.count(a))