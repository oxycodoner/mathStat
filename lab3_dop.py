import numpy as np
from scipy import stats
import random


def calculateMathWait(array:list):
    math_wait = sum(array) / n
    return math_wait


def calculateDispersion(array:list, math_wait):
    newArr = []
    for i in array:
        newArr.append((i - math_wait) ** 2)
    dispersion = sum(newArr) / n
    newArr.clear()
    return dispersion


def exponential_distribution(beta):
    result = []
    for i in range(n):
        rand = - beta * np.log(random.random())
        result.append(rand)

    return result


def pirsonCriterion(empericArray:list, p, numOfGaps):
    y = stats.expon.rvs(scale=p, size=n)

    down_emp = np.min(y)
    up_emp = np.max(y)
    gap = (up_emp - down_emp) / numOfGaps

    observed = []
    temp = down_emp
    while temp < up_emp:
        counter = 0
        for i in empericArray:
            if temp <= i < temp+gap:
                counter += 1
        temp += gap
        observed.append(counter)

    # print(np.sort(empericArray), '\n', observed)

    expected = []
    temp = down_emp
    while temp < up_emp:
        counter = 0
        for i in y:
            if temp <= i < temp + gap:
                counter += 1
        temp += gap
        expected.append(counter)

    # print(np.sort(y), '\n', expected)

    chi = stats.chisquare(observed, expected, ddof=(numOfGaps-1))
    print(observed, '\n', expected, '\n', chi, '\nСтепеней свободы: ', n - 1)


n = 1000
beta = 3

geomDistrArr = exponential_distribution(beta)
print("Геометрическое распределение №1\nМатематическое ожидание = ", calculateMathWait(geomDistrArr))
print("Дисперсия = ", calculateDispersion(geomDistrArr, calculateMathWait(geomDistrArr)), "\n")


pirsonCriterion(geomDistrArr, beta, 14)

geomDistrArr.clear()