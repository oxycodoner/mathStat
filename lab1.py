import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from scipy.stats import norm

matplotlib.style.use('grayscale')

n = 10  # число испытаний
randomizedArray = []
for i in range(n):
    randomizedArray.append(random.random())  # псевдослучайные величины, вырабатываемые
    # датчиком случайных чисел

# print("Массив псевдослучайных чисел = ", randomizedArray)
# print(a[2])

math_wait = (sum(randomizedArray)) / n  # математическое ожидание
print("Математическое ожидание = ", math_wait)

newArr = []
for i in randomizedArray:
    newArr.append((i - math_wait) ** 2)

dispersion = sum(newArr) / n  # дисперсия
srednekvadr_otkl = math.sqrt(dispersion)  # среднеквадратичное отклонение
newArr.clear()
print("Эмпирическая дисперсия = ", dispersion, "\nСредне квадратичное отклонение = ", srednekvadr_otkl)

korr = []
for f in range(1, n):  # коэффициенты корреляции
    up_sum = 0
    down_sum = 0
    for i in range(n - f - 1):
        up_sum += ((randomizedArray[i] - math_wait) * (randomizedArray[i + f] - math_wait))
    for i in range(n):
        down_sum += ((randomizedArray[i] - math_wait) ** 2)

    korr.append(up_sum / down_sum)

# print("Коэффициенты корреляции = ", korr)

x = range(len(korr))
ax = plt.gca()
ax.bar(x, korr, align='edge')
str_ = 'Коррелограмма, N = ' + str(n)
plt.xlabel(str_)
plt.show()

# интегральная функция распределения
minV = 0.0
maxV = 1.0
numOfParts = 100
delta = (maxV - minV) / (numOfParts)
fun = [0 for i in range(numOfParts)]
for i in range(numOfParts):
    for j in randomizedArray:
        if (minV + delta * i) <= j < (minV + delta * (i + 1)):
            fun[i] += 1
for i in range(numOfParts):
    fun[i] /= n
distribFun = [0 for i in range(numOfParts)]
for i in range(numOfParts):
    for j in range(i, -1, -1):
        distribFun[i] += fun[j]
for i in range(numOfParts):
    plt.bar((minV + delta * i) + delta / 2, distribFun[i], width=delta)

str_ = 'Функция распределения, N = ' + str(n)
plt.xlabel(str_)
plt.show()

s = pd.Series(randomizedArray)  # график функции плотности распределения
s.plot.hist()
str_ = 'Функция плотности, N = ' + str(n)
plt.xlabel(str_)
plt.show()

randomizedArray.clear()
korr.clear()
