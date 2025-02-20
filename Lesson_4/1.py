print("Координаты точки A(x1;y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("Координаты точки B(x2;y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(" y = %.2f*x + %.2f" % (k, b))

import timeit
print(timeit.timeit("x = 2 + 2"))
print(timeit.timeit("x = sum(range(10))"))

cProfile.run('main()')