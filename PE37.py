import time
import math
start_time = time.time()
primes = []
def sieveOfE(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(2*p, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n+1):
        if prime[p]:
            primes.insert(-1,p)
def isPrime(n):
    if n == 1:
        return False
    maxD = int(math.sqrt(n))+1
    for i in range(2,maxD):
        if n%i == 0:
            return False
    return True
def isTruncatablePrimeLeft(n):
    if len(str(n)) == 1:
        return False
    for i in range(len(str(n))):
        num = int(str(n)[0:len(str(n))-i])
        if not isPrime(num):
            return False
    return True
def isTruncatablePrimeRight(n):
    if len(str(n)) == 1:
        return False
    for i in range(len(str(n))):
        num = int(str(n)[i:len(str(n))])
        if not isPrime(num):
            return False
    return True
sieveOfE(740000)
numberOfTP = 0
sumOfTP = 0
for i in primes:
    if numberOfTP == 11:
        break
    if isTruncatablePrimeRight(i) and isTruncatablePrimeLeft(i):
        print(i)
        numberOfTP+=1
        sumOfTP+=i
print(sumOfTP)
print("--- %s seconds ---" % (time.time() - start_time))