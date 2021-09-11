input_no=int(input("Enter a number"))

def sumofno_(no):
    sum=0
    for i in range(no+1):
        if i%3==0 or i%5==0 : 
            sum+=i
    return sum

sumof=sumofno_(input_no)
print(sumof)
