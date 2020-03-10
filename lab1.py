import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from scipy.stats import norm

matplotlib.style.use('grayscale')

n = 100  # число испытаний
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

# функция распределения
minV = 0.0
maxV = 1.0
numOfParts = 100
delta = (maxV - minV) / (numOfParts)
function = [0 for i in range(numOfParts)]
for i in range(numOfParts):
    for j in randomizedArray:
        if (minV + delta * i) <= j < (minV + delta * (i + 1)):
            function[i] += 1
for i in range(numOfParts):
    function[i] /= n
distributionFunction = [0 for i in range(numOfParts)]
for i in range(numOfParts):
    for j in range(i, -1, -1):
        distributionFunction[i] += function[j]
for i in range(numOfParts):
    plt.bar((minV + delta * i) + delta / 2, distributionFunction[i], width=delta)

plt.xlabel("Функция распределения, N = " + str(n))
plt.show()

s = pd.Series(randomizedArray)  # функция плотности распределения
s.plot.hist()
plt.xlabel("Функция плотности, N = " + str(n))
plt.show()

function.clear()
distributionFunction.clear()
randomizedArray.clear()
korr.clear()
