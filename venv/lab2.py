import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

def uniformDistrib (r_low, r_up):
    uniformDitribArray = [(r_up - r_low + 1) * random.random() + r_low for i in range(n)]
    graphics(uniformDitribArray, r_low, r_up)
    return uniformDitribArray


def calculateMathWait (array:list):
    math_wait = sum(array) / n
    return math_wait


def calculateDispersion (array:list, math_wait):
    newArr = []
    for i in array:
        newArr.append((i - math_wait) ** 2)
    dispersion = sum(newArr) / n
    newArr.clear()
    return dispersion


def binomDistr (p, N):
    array = []
    for i in range(n):
        M = random.random()
        P = (1 - p) ** N
        m = 0

        M -= P
        while M >= 0:
            P *= ((N - m) / (m + 1)) * (p / (1 - p))
            m += 1
            M -= P

        array.append(m)

    graphics(array, 0, N)
    return array


def binomDistrWithNormApprox (p, N):
    array = []
    for i in range(n):
        array.append(np.math.floor(np.random.normal(N*p, np.sqrt(N*p*(1.0-p))) + 0.5))

    graphics(array, 0, N)
    return array


def geomDistr (p):
    array = []
    maxV = 1
    for i in range(1, n):
        M = random.random()
        P = p
        m = 1

        M -= P
        while M >= 0:
            P *= (1 - p)
            m += 1
            M -= P
        if maxV < m :
            maxV = m
        array.append(m)

    graphics(array, 1, maxV)
    return array


def geomDistrNum2 (p):
    array = []
    maxV = 1
    for i in range(1, n):
        m = 1
        randNum = random.random()
        while randNum > p :
            randNum = random.random()
            m += 1
        if maxV < m :
            maxV = m
        array.append(m)

    graphics(array, 1, maxV)
    return array


def geomDistrNum3 (p):
    array = []
    maxV = 1
    for i in range(1, n):
        rand = random.random()
        x = int(np.log(rand) / np.log(1 - p)) + 1
        if maxV < x :
            maxV = x
        array.append(x)

    graphics(array, 1,maxV)
    return array


def puassonDistrNum1 (mu):
    array = []
    maxV = 1
    for i in range(1, n):
        if mu >= 88 :
            m = np.math.floor(random.normalvariate(mu, mu))
        else:
            M = random.random()
            P = np.exp(-mu)
            m = 0

            M -= P
            while M >= 0:
                m += 1
                P *= (mu / m)
                M -= P

        if maxV < m :
            maxV = m
        array.append(m)

    graphics(array, 0, maxV)
    return array


def puassonDistrNum2 (mu):
    array = []
    maxV = 1
    for i in range(0, n):
        if mu >= 88 :
            x = np.math.floor(random.normalvariate(mu, mu))
        else:
            randNum = random.random()
            x = 0
            while randNum >= np.exp(-mu):
                randNum = randNum * random.random()
                x += 1
        if maxV < x :
            maxV = x
        array.append(x)
    graphics(array, 0, maxV)
    return array


def logarithmDistr (p):
    array = []
    maxV = 1
    for i in range(1, n):
        px = - p / np.log(1 - p)
        randNum = random.random()
        x = 1
        while True:
            randNum -= px
            if randNum < 0:
                if maxV < x :
                    maxV = x
                array.append(x)
                break
            px = px * x * p / (x + 1)
            x += 1
    graphics(array, 1, maxV)
    return array


def functionProbability (array:list, minV, maxV):
    numOfParts = 100
    delta = (maxV - minV) / (numOfParts)
    function = [0 for i in range(numOfParts)]
    for i in range(numOfParts):
        for j in array:
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


def graphics (array:list, minV, maxV):
    functionProbability(array, minV, maxV)
    plt.xlabel("Функция распределения")
    plt.show()
    s = pd.Series(array)
    s.plot.hist()
    plt.xlabel("Функция плотности")
    plt.show()

n = 10000

unifDistrArr = uniformDistrib(1, 100)
print("Равномерное распределение\nМатематическое ожидание = ", calculateMathWait(unifDistrArr))
print("Дисперсия = ", calculateDispersion(unifDistrArr, calculateMathWait(unifDistrArr)), "\n")
unifDistrArr.clear()

binomDistrArr = binomDistr(0.5, 100)
print("Биномиальное распределение №1\nМатематическое ожидание = ", calculateMathWait(binomDistrArr))
print("Дисперсия = ", calculateDispersion(binomDistrArr, calculateMathWait(binomDistrArr)), "\n")
binomDistrArr.clear()

binomDistrArr2 = binomDistrWithNormApprox(0.5, 100)
print("Биномиальное распределение №2\nМатематическое ожидание = ", calculateMathWait(binomDistrArr2))
print("Дисперсия = ", calculateDispersion(binomDistrArr2, calculateMathWait(binomDistrArr2)), "\n")
binomDistrArr2.clear()

geomDistrArr = geomDistr(0.5)
print("Геометрическое распределение №1\nМатематическое ожидание = ", calculateMathWait(geomDistrArr))
print("Дисперсия = ", calculateDispersion(geomDistrArr, calculateMathWait(geomDistrArr)), "\n")
geomDistrArr.clear()

geomDistrArr2 = geomDistrNum2(0.5)
print("Геометрическое распределение №2\nМатематическое ожидание = ", calculateMathWait(geomDistrArr2))
print("Дисперсия = ", calculateDispersion(geomDistrArr2, calculateMathWait(geomDistrArr2)), "\n")
geomDistrArr2.clear()

geomDistrArr3 = geomDistrNum3(0.5)
print("Геометрическое распределение №3\nМатематическое ожидание = ", calculateMathWait(geomDistrArr3))
print("Дисперсия = ", calculateDispersion(geomDistrArr3, calculateMathWait(geomDistrArr3)), "\n")
geomDistrArr3.clear()

puassonDistrArr1 = puassonDistrNum1(10)
print("Пуассоновское распределение №1\nМатематическое ожидание = ", calculateMathWait(puassonDistrArr1))
print("Дисперсия = ", calculateDispersion(puassonDistrArr1, calculateMathWait(puassonDistrArr1)), "\n")
puassonDistrArr1.clear()

puassonDistrArr2 = puassonDistrNum2(10)
print("Пуассоновское распределение №2\nМатематическое ожидание = ", calculateMathWait(puassonDistrArr2))
print("Дисперсия = ", calculateDispersion(puassonDistrArr2, calculateMathWait(puassonDistrArr2)), "\n")
puassonDistrArr2.clear()

logDistrArr = logarithmDistr(0.5)
print("Логарифмическое распределение\nМатематическое ожидание = ", calculateMathWait(logDistrArr))
print("Дисперсия = ", calculateDispersion(logDistrArr, calculateMathWait(logDistrArr)), "\n")
logDistrArr.clear()