
def factor():
    n=int(input("please enter a whole number:"))
    fact=1
    for factor in range(1,n+1):
        fact=fact*5
    print("The factorial of",n,"is",fact)


factor()