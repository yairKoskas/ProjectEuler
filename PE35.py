import time
st = time.time()

primes = []
def sieveOfEWithoutEvens(n):
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
        if prime[p] and withoutEvens(p):
            primes.insert(-1,p)


def withoutEvens(p):
    if p == 2:
        return True
    for i in str(p):
        if int(i)%2 == 0:
            return False
    return True




def checkCycle(p):
    length = len(str(p))
    for i in range(length-1):
        dig = p%10 * (10**(length-1))
        p = int(p/10)
        p += dig
        if p not in primes:
            return 0
    return 1


sieveOfEWithoutEvens(1000000)
x = 0
for i in primes:
    x += checkCycle(i)
print(x)
print("--------{} ms-----------".format(time.time()-st))