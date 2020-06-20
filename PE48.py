import time
start = time.time()
sum = 0
for i in range(1,1000):
    sum += (i**i)%(10**10)
print(sum%(10**10))
print("--- %s seconds ---" % (time.time() - start))