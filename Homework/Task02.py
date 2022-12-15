<<<<<<< HEAD
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

from random import randint

x = randint(0, 1)
y = randint(0, 1)
z = randint(0, 1)

print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
if not (x or y or z) == (not x and not y and not z):
    print('Выражение верно!')
else:
=======
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

from random import randint

x = randint(0, 1)
y = randint(0, 1)
z = randint(0, 1)

print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
if not (x or y or z) == (not x and not y and not z):
    print('Выражение верно!')
else:
>>>>>>> 38d518edd7576fa256c250883a17b84c37e7a701
    print('Выражение неверно!')