import time
st = time.time()
def digFifthPow(n):
    n = str(n)
    length = len(n)
    sum = 0
    for i in range(length):
        sum += int(n[i])**5
    return sum
x = 0
for i in range(354295):
    if digFifthPow(i) == i:
        x += i
print('sum={}'.format(x))
print("--------{} ms-----------".format(time.time()-st))