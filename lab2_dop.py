# пирсон геометрич р = 0.7
import numpy as np
from scipy import stats
import random


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
    return array


def pirsonCriterion (empericArray:list, p):
    observed = np.bincount(empericArray)[1:]
    expected = [n*stats.geom.pmf(x, p) for x in range(1, max(empericArray) + 1)]
    chi = stats.chisquare(observed, expected, ddof=(n-1))
    print(observed, '\n', expected, '\n', chi, '\nСтепеней свободы: ', n -1)


n = 29
p = 0.7

geomDistrArr = geomDistr(p)
print("Геометрическое распределение №1\nМатематическое ожидание = ", calculateMathWait(geomDistrArr))
print("Дисперсия = ", calculateDispersion(geomDistrArr, calculateMathWait(geomDistrArr)), "\n")


pirsonCriterion(geomDistrArr, p)

geomDistrArr.clear()