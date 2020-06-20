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
sieveOfE(1000000)
index = 0
for i in primes:
    if i > 1000000:
        print(index)
    index+=1
