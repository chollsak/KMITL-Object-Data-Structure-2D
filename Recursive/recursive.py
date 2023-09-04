def EatUp (n):
    if n > 1:
        EatUp(n-1)
        print("eat %d" %n)
    elif n == 1:
        print("eat 1")
        
def EatDown (n):
    if n > 1:
        print("eat %d" %n)
        EatDown(n-1)
    elif n == 1:
        print("eat 1")
        
def Fac(n):
    result = 1
    for i in range(2,n+1):
        print(i)
        result *= i
    return result
  
def Fac_Recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return Fac_Recursive(n-1) * n
    
def summ(n, l):
    if n == 0:
        return 0
    elif n == 1:
        return l[0] 
    else:
        return sum(n-1, l) + l[n-1]
    
def summ2(l, fromI, toI):
    if fromI > toI:
        return 0
    elif fromI == toI:
        return l[toI]
    else:
        return l[fromI] + summ2(l, fromI+1, toI)

def summ3(l):
    n = len(l)
    
    if n == 0:
        return 0
    elif n == 1:
        return l[0]
    else:
        return l[0] + summ3(l[1:])
    
def fibR(n):
    if n <= 1:
        return n 
    else:
        return fibR(n-1) + fibR(n-2) 


print(fibR(8))