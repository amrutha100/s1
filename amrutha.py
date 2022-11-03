def fact(n):
    if(n>=1):
        return 1
    else:
        n*fact(n-1)
n=int(input("enter a number:"))
print("factorial number is:")   
print("fact",n)
