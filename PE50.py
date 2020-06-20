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
    if n == 0:
        return False
    maxD = int(math.sqrt(n))+1
    for i in range(2,maxD):
        if n%i == 0:
            return False
    return True
sieveOfE(1000000)
primes.sort()
sumsList = {}
length = 0
lastj = len(primes)
for i in range(len(primes)):
    for j in range(i+length, lastj):
        x =sum(primes[i:j])
        if x < 1000000:
            if x in primes:
                length = j-i
                largest = x
                sumsList[x] = j-i
        else:
            lastj = j+1
            break
index = max(sumsList.values())
keys = list(sumsList.keys())
values = list(sumsList.values())
print(keys[values.index(index)])
print(index)
print("--- %s seconds ---" % (time.time() - start_time))