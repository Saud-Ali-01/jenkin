import random
c = random.choice([1,-1,0])
computer = c
choice = {
    "rock":1,"paper":0,"scesior":-1,
} 
comput = {
    1:"rock",0:"paper",-1:"scesior",
} 
user = input("Enter your choice .")
print(f"you choice {user} and computer choice {comput[computer]}")
if(computer == choice[user]):
    print("Draw")
else:
    if(choice[user]==1 and computer==0):
      print("your defeat")
    elif(choice[user]==0 and computer==1):
      print("your won")
    elif(choice[user]==1 and computer==-1):
       print("your defeat")
    elif(choice[user]==-1 and computer==1):
         print("your won")
    elif(choice[user]==-1 and computer==0):
         print("your defeat")
    elif(choice[user]==0 and computer==-1):
       print("your won")