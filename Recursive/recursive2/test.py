def summ(n, l):
    if n == 0:
        return 0
    elif n == 1:
        return l[0]
    else:
        return summ(n-1, l) + l[n-1]
    
l = [1,2,3,4,5,6,7,8,9]
print(summ(len(l),l))