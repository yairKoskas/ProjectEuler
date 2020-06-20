import math
count = 0
sum = 0
lengths = [0 for x in range(1001)]
for m in range(2,int(math.sqrt(1001/2))+1):
    for n in range(1,m):
        if (n + m)%2 == 1 and math.gcd(n, m) == 1:
            b = m*m - n*n
            a = 2*m*n
            c = m*m+n*n
            L = a+b+c
            while L <= 1000:
                lengths[L]+=1
                L = L+(a+b+c)
print(lengths.index(8))