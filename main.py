import math
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = b**2 - 4 * a * c
if d == 0:
    print("Уравнение имеет 1 корень")
    x = -(b/2 * a)
    print("Корень уравнения равен:", x)
elif d < 0:
    print("Уравнение не имеет корней")
else:
    print("Уравнение имеет 2 корня")
    x1 = -((b + math.sqrt(d))/2 * a)
    x2 = -((b - math.sqrt(d))/2 * a)
    print("Первый корень уравнения равен:", x1)
    print("Второй корень уравнения равен:", x2)
