import math
def isPrime(n):
    if n == 1:
        return False
    maxD = int(math.sqrt(n))+1
    for i in range(2,maxD):
        if n%i == 0:
            return False
    return True
def numOfDistinctFactors(n):
    count=0
    for i in range(2,n):
        if n%i == 0 and isPrime(i):
            count+=1
    return count
notFound = True
x = 650
while notFound:
    if numOfDistinctFactors(x) == 4:
        x += 1
        if numOfDistinctFactors(x) == 4:
            x += 1
            if numOfDistinctFactors(x) == 4:
                x += 1
                if numOfDistinctFactors(x) == 4:
                    print(x-3)
                    break
    x += 1