import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt

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

def uniformDistribution (a, b):
    result = [((b - a) * random.random() + a) for i in range(n)]
    graphics(result, np.min(result), np.max(result))
    return result


def normalDidtribution_CLT(m, sigma):
    result = []
    count = 12
    for i in range(n):
        uniform_sample = np.random.random_sample(count)
        rand = m + sigma * (np.sum(uniform_sample) - count / 2) / np.sqrt(count / 12)
        result.append(rand)

    graphics(result, np.min(result), np.max(result))
    return result


def normalDidtribution_BoxMiller():
    result = []
    for i in range(math.ceil((float(n) / 2))):
        u1 = np.random.random_sample(1)
        u2 = np.random.random_sample(1)
        rand1 = np.sqrt(- 2 * np.log(u2)) * np.cos(2 * np.pi * u1)
        rand2 = np.sqrt(- 2 * np.log(u2)) * np.sin(2 * np.pi * u1)
        result.append(rand1[0])
        result.append(rand2[0])

    graphics(result, np.min(result), np.max(result))
    return result


def exponential_distribution(beta):
    result = []
    for i in range(n):
        rand = - beta * np.log(random.random())
        result.append(rand)

    graphics(result, np.min(result), np.max(result))
    return result


def chisquare_distribution(degrees):
    result = []

    for i in range(n):
        rand = 0
        for j in range(degrees):
            rand += np.random.normal(0, 1) ** 2

        result.append(rand)

    graphics(result, np.min(result), np.max(result))
    return result


def student_distribution(param):
    result = []

    for i in range(n):
        rand = np.random.normal(0, 1) / np.sqrt(np.random.chisquare(param) / param)

        result.append(rand)

    graphics(result, np.min(result), np.max(result))
    return result


def functionProbability(array:list, minV, maxV):
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


def graphics(array:list, minV, maxV):
    functionProbability(array, minV, maxV)
    plt.xlabel("Функция распределения")
    plt.show()
    s = pd.Series(array)
    s.plot.hist()
    plt.xlabel("Функция плотности")
    plt.show()


n = 10000

unifDistrArr = uniformDistribution(1, 2)
print("Равномерное распределение\nМатематическое ожидание = ", calculateMathWait(unifDistrArr))
print("Дисперсия = ", calculateDispersion(unifDistrArr, calculateMathWait(unifDistrArr)), "\n")
unifDistrArr.clear()

normalDistrArr = normalDidtribution_CLT(0, 1)
print("Нормальное распределение №1\nМатематическое ожидание = ", calculateMathWait(normalDistrArr))
print("Дисперсия = ", calculateDispersion(normalDistrArr, calculateMathWait(normalDistrArr)), "\n")
normalDistrArr.clear()

normalDistrArr = normalDidtribution_BoxMiller()
print("Нормальное распределение №2\nМатематическое ожидание = ", calculateMathWait(normalDistrArr))
print("Дисперсия = ", calculateDispersion(normalDistrArr, calculateMathWait(normalDistrArr)), "\n")
normalDistrArr.clear()

expDistrArr = exponential_distribution(10)
print("Экспоненциальное распределение\nМатематическое ожидание = ", calculateMathWait(expDistrArr))
print("Дисперсия = ", calculateDispersion(expDistrArr, calculateMathWait(expDistrArr)), "\n")
expDistrArr.clear()

chisquareDistrArr = chisquare_distribution(10)
print("Хи-квадрат распределение\nМатематическое ожидание = ", calculateMathWait(chisquareDistrArr))
print("Дисперсия = ", calculateDispersion(chisquareDistrArr, calculateMathWait(chisquareDistrArr)), "\n")
chisquareDistrArr.clear()

studentDistrArr = student_distribution(10)
print("Распределение Стьюдента\nМатематическое ожидание = ", calculateMathWait(studentDistrArr))
print("Дисперсия = ", calculateDispersion(studentDistrArr, calculateMathWait(studentDistrArr)), "\n")
studentDistrArr.clear()