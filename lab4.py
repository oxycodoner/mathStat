import numpy as np
import random

N = 1000
m = 3
lamb = [0.00004, 0.00001, 0.00008]
T = 8760
L = [3, 4, 4]

failtureTime = [np.zeros(4), np.zeros(2), np.zeros(6)]
d = 0

for n in range(1, N+1):
    for array in range(len(failtureTime)):
        for time in range(len(failtureTime[array])):
            failtureTime[array][time] = - np.log(random.random()) / lamb[array]

        for i in range(L[array]):
            brokenIndex = list(failtureTime[array]).index(min(failtureTime[array]))
            failtureTime[array][brokenIndex] -= np.log(random.random()) / lamb[array]

    if not (((failtureTime[0][0] > T and failtureTime[0][1] > T)
            or (failtureTime[0][2] > T and failtureTime[0][3] > T))
            and (failtureTime[1][0] > T and failtureTime[1][1] > T)
            and ((failtureTime[2][0] > T and failtureTime[2][1] > T) or (failtureTime[2][2] > T and failtureTime[2][3] > T)
            or (failtureTime[2][4] > T and failtureTime[2][4] > T))):
        d += 1

print('L = ', L)
print('P = ', 1 - float(d) / float(N))

