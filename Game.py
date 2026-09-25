import random
a = random.randint(1,99)
count=0
while(True):
   n= int(input("Enter your no. "))
   if (n>a):
       print(f"your value is {n} greater than computer value") 
       count+=1
   elif(n<a):
       print(f"your value is {n} smaller than computer value") 
       count+=1
   elif(n== a):
       print(f"your is {n} and computer value is {a}")
       count+=1
       break
print(f"toatal try to guess the no. is {count}")
   
       
       