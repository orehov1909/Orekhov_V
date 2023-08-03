from math import sqrt

a, b, c = map(int,
              input("Введите коэффиценты квадратного уравнения: ").split())
d = b ** 2 - 4 * a * c
if d < 0:
    print("Корней нет")