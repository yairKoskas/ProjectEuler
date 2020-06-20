import time
start = time.time()

def isContainingSameDigits(a, b):
    arrA = [0,0,0,0,0,0,0,0,0,0]
    arrB = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(str(a))):
        arrA[int(str(a)[i])]+=1
    for i in range(len(str(b))):
        arrB[int(str(b)[i])]+=1
    for i in range(len(arrA)):
        if (arrA[i] == 0 and arrB[i] != 0) or (arrB[i] == 0 and arrA[i] != 0):
            return False
    return True
a = 1
notFound = True
while(notFound):
    if isContainingSameDigits(a,2*a):
        if(isContainingSameDigits(2*a,3*a)):
            if(isContainingSameDigits(3*a,4*a)):
                if(isContainingSameDigits(4*a,5*a)):
                    if(isContainingSameDigits(5*a,6*a)):
                        print(a)
                        break
    a+=1
print("--- %s seconds ---" % (time.time() - start))

