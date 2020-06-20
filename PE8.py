f = open("number.txt","r")
def multOfDigits(s):
    n = 1
    for i in range(len(s)):
        n*=int(s[i])
    return n
maxMult = 0
for line in f:
    for i in range(1000-13):
        s = line[i:i+13]
        mult = multOfDigits(s)
        if multOfDigits(s) > maxMult:
            print(s)
            maxMult = multOfDigits(s)
print('largest is '+str(maxMult))