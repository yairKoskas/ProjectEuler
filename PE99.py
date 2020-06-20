import math
f = open("p099_base_exp.txt","r")
maxNumber = 0
a = 0
b = 0
aExp = 0
bExp = 0
maxLine = 0
for i in f.readlines():
    for let in str(i):
        while let != ',':
            a += let
        a = int(a)