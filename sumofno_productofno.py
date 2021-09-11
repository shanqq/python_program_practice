input_no=int(input("Enter 1 for sum of number and 2 for product of number: "))


def sumofno():
    sum1=0
    n=int(input("enter number: "))
    for i in range(1,n+1):
        sum1=sum1+i
    return sum1

def prodofno():
    prod=1
    n1=int(input("enter a number: "))
    for i in range(1,n1+1):
        prod=prod*i
    return prod

def sum_OR_prod(no):
    if no==1:
        print(sumofno())
    elif no==2:
        print(prodofno())
    else:
        print("Invalid input")

sum_OR_prod(input_no)
