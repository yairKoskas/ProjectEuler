import time
import math
start_time = time.time()
collatzNumber = {1: 1}


def collatzNumbersLength(n):
    if math.log(n,2).is_integer():
        collatzNumber[n] = math.log(n, 2)
        return math.log(n, 2)
    if n in collatzNumber:
        return int(collatzNumber[n])
    if n % 2 == 0:
        collatzNumber[n] = collatzNumbersLength(int(n / 2)) + 1
        return collatzNumbersLength(int(n / 2)) + 1
    else:
        collatzNumber[n] = collatzNumbersLength(int((3 * n + 1) / 2)) + 1
        return collatzNumbersLength(int((3 * n + 1) / 2)) + 1


maxNum = 0
maxKey = 0
for i in range(1,1000000):
    if collatzNumbersLength(i) > maxNum:
        maxNum = collatzNumbersLength(i)
        maxKey = i
print(maxKey)
print("--- %s seconds ---" % (time.time() - start_time))
