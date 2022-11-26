import random as r
def oddeven(n):
    if n%2==0:
        print(n,"is a even number")
    else:
        print(n,"is a odd number")
def posneg(n):
    if n>=0:
        print(n,"is a positive number")
    else:
        print(n,"is a negative number")
def comprime(n):
    s=0
    for i in range(2,n):
        if n%i==0:
            s+=1
    if s==0:
        print(n,"is a prime number")
    else:
        print(n,"is a composite number")


a=int(input("Enter starting of the range:"))
b=int(input("Enter end of the range:"))
n=r.randint(a,b)
oddeven(n)
posneg(n)
comprime(n)

