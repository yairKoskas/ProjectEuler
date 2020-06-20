import itertools
import math
import time
start_time = time.time()
sevens = [1,2,3,4,5,6,7]
def isPrime(n):
    maxD = int(math.sqrt(n))
    for i in range(2,maxD):
        if n%i == 0:
            return False
    return True
def numFromDig(digits):
    digits = list(digits)
    sum = 0
    for i in range(len(digits)):
        sum += digits[i] * (10**i)
    return sum
def permutationList(l):
    permlist = list(itertools.permutations(l))
    return permlist

permlist = permutationList(sevens)
maxPrime = 0
for i in permlist:
    if int(str(numFromDig(i))[0])%2 == 0 or int(str(numFromDig(i))[0])%5 == 0:
        continue
    if  numFromDig(i) > maxPrime and isPrime(numFromDig(i)):
        maxPrime = numFromDig(i)
print(maxPrime)
print("--- %s seconds ---" % (time.time() - start_time))