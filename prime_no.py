n=int(input("Enter number upto which you want to find prime no."))
for i in range(2,n+1):
    count=0
    for j in range(2,(i//2)+1):
        if i == 2:
            print(i)
            break
        elif i%j == 0:
            count=1
            break
        else:
            pass
    if count == 0:
        print(i)


