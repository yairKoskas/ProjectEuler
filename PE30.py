def digFifthPow(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])**5
    return sum
l = []
for i in range(pow(10,6)):
    if digFifthPow(i) == i:
        print(i)
        l.insert(-1,i)
print('sum='+str(sum(l)))