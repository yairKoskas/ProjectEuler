import math
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