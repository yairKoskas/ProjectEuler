import math
import time
start_time = time.time()
l = [x*(x+1)/2 for x in range(50000)]
def numOfDivisors(n):
    count = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            count+=2
    return count
i = 0
while(True):
    if numOfDivisors(int((i*(i+1))/2)) > 500:
        print(int((i*(i+1))/2))
        break
    i+=1
print("--- %s seconds ---" % (time.time() - start_time))