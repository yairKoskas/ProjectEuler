import math
import time
start = time.time()
partitions = {0:1,1:1,2:2,3:3,4:5,5:7,6:11,7:15,8:22,9:30}
def partition(n):
    if n in partitions.keys():
        return partitions[n]
    if n<0:
        return 0
    sum = 0
    r1 = int(-(math.sqrt(24*n+1)-1)/6)
    r2 = int((math.sqrt(24*n+1)+1)/6)
    for i in range(r1,r2+1):
        if i == 0:
            continue
        sum += int((-1)**(i+1) * partition(n - int((i*(3*i-1)/2))))
    partitions[n] = sum % 1000000
    return sum % 1000000
notFound = True
i = 0
while notFound:
    if partition(i) == 0:
        break
    i+=1
print(i)
print("--- %s seconds ---" % (time.time() - start))