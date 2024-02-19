import math

def feladat1(a, b):
    return math.gcd(a, b)

def feladat2(a,b):
    c = []
    for i in range(len(a)):
            c.append(feladat1(a[i],b[i]))
    return c        
    
def feladat3():
    l1 = []
    l2 = []
    for i in range(2):
        for x in range(5):
            if i+1 == 1:
                l1.append(int(input(str(i+1)+". Lista | "+str(x+1) + ". Szám: ")))
            if i+1 == 2: 
                l2.append(int(input(str(i+1)+". Lista | "+str(x+1) + ". Szám: ")))
            
            
    return feladat2(l1,l2)    
       
print(feladat3())    