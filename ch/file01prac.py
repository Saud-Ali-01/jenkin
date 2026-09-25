import random
def game():
    a =random.randint(1,34)
    # print(f"your score {a}")
    with open("Score.txt") as f:
        c= f.read()
        if (c != ""):
            c= int(c)
        else:
            c= 0
    print(f"your score {a}")
    if (a>c):
        with open("Score.txt","w") as f:
            f.write(str(a))   
    return c
game()

        
    
