def printer(a):
    for i in range(a):
        print(i)
def wish(a):
    print("i wish  "+a)
# wish("bike")
def sum(a,b):
    c = a+b
    print("the sum of a and b",c)
# sum(3,4)
def goodDay(name, we="bye"):
    print(f" your name {name}")
    print(we)
# goodDay(1,"saud")
def factorial(n):
    if(n==1):
            print("*")
    if(n==1):
        return 1
    factorial(n-1)
    print("*"*n,end="")
    print("")
factorial(4)