import random

num = random.randint(1, 10)

tries = 0

while  True: 

    guess = int(input("please guess ur number :"))

    if num == guess:
        tries += 1
        print(f"u r a genius and u guessed it in {tries} tries4")
        break
    
    elif num > guess :
        tries += 1
        print("go a little higher ")
        
    elif num < guess :
        tries += 1
        print("go a little lower ")

    else:
        tries += 1
        print("u r a loser")