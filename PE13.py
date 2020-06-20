f = open("PE13.txt","r")
sum = 0
for line in f.readlines():
    sum+=int(line)
print(int(sum/(10**(len(str(sum))-10))))