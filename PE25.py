import time
start = time.time()


def Fib(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w



def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1],
         [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if (n % 2 != 0):
        multiply(F, M)
notFound = True
lowerBound = 0
upperBound = 0
index = 0
while(notFound):
    if len(str(Fib(2**index))) < 1000:
        index+=1
    else:
        upperBound = 2**index
        lowerBound = 2**(index-1)
        notFound = False
for i in range(lowerBound,upperBound+1):
    if len(str(Fib(i))) == 1000:
        print(i)
        break
print("--- %s seconds ---" % (time.time() - start))