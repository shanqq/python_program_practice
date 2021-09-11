name=input("Enter your name")

print("",end="")
def greeting(name):
    if name == "Alice" or name == "Bob":
        print("hello {} ".format(name))
    else:
        print("you are not Alice or Bob")

greeting(name)

